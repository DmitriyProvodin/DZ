import os
import requests
from typing import Any
from logger_config import setup_logger
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

logger = setup_logger("external_api", "external_api.log")


def convert_to_rub(transaction: dict[str, Any]) -> float:
    """
    Принимает транзакцию и возвращает сумму в рублях.
    Если валюта USD или EUR — конвертирует по актуальному курсу.
    """
    amount = transaction.get("operationAmount", {}).get("amount")
    currency = transaction.get("operationAmount", {}).get("currency", {}).get("code")

    if amount is None or currency is None:
        logger.warning("Некорректная транзакция: отсутствуют amount или currency")
        return 0.0

    if currency == "RUB":
        return float(amount)

    api_key = os.getenv("EXCHANGE_API_KEY")
    if not api_key:
        logger.error("API ключ для конвертации валют не найден в переменных окружения.")
        return 0.0

    url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}&symbols=RUB"

    headers = {
        "apikey": api_key
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data: dict[str, Any] = response.json()
        rate = data["rates"]["RUB"]
        converted_amount = float(amount) * rate
        logger.info(f"Конвертация {amount} {currency} в рубли: {converted_amount:.2f}")
        return round(converted_amount, 2)
    except (requests.RequestException, KeyError) as e:
        logger.error(f"Ошибка при конвертации валюты: {e}")
        return 0.0
