import os
import requests
from typing import Dict
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("EXCHANGE_API_KEY")


def convert_to_rub(transaction: Dict) -> float:
    """
    Конвертирует сумму транзакции в рубли.
    Если валюта RUB — возвращает сумму напрямую.
    Если USD или EUR — делает запрос к внешнему API.

    :param transaction: словарь с транзакцией
    :return: сумма в рублях
    """
    try:
        amount = float(transaction["operationAmount"]["amount"])
        currency = transaction["operationAmount"]["currency"]["code"]

        if currency == "RUB":
            return amount

        url = "https://api.apilayer.com/exchangerates_data/latest"
        params = {
            "base": currency,
            "symbols": "RUB"
        }
        headers = {
            "apikey": API_KEY
        }

        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        result = response.json()
        rate = result["rates"]["RUB"]

        return round(amount * rate, 2)

    except Exception:
        return 0.0
