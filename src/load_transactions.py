import json
import logging
from pathlib import Path
from typing import Any

import pandas as pd

# 🔹 Создание логгера для модуля load_transactions
logger = logging.getLogger("load_logger")

# 🔹 Установка уровня логов
logger.setLevel(logging.DEBUG)

# 🔹 Настройка file_handler
file_handler = logging.FileHandler("../Logs/load_transactions.log", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# 🔹 Настройка форматтера
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)

# 🔹 Добавление обработчика к логгеру
logger.addHandler(file_handler)


def load_transactions(filepath: str) -> list[dict[str, Any]]:
    """
    Загружает список транзакций из файла JSON, CSV или XLSX.
    :param filepath: Путь к файлу.
    :return: Список транзакций в виде словарей.
    """
    path = Path(filepath)

    if not path.exists():
        logger.error(f"Файл не найден: {filepath}")
        raise FileNotFoundError(f"Файл не найден: {filepath}")

    try:
        if path.suffix == ".json":
            with open(filepath, encoding="utf-8") as f:
                data = json.load(f)
                logger.debug(f"Загружено {len(data)} транзакций из JSON.")
                return data

        elif path.suffix == ".csv":
            df = pd.read_csv(filepath)
            logger.debug(f"Загружено {len(df)} транзакций из CSV.")
            return df.to_dict(orient="records")

        elif path.suffix == ".xlsx":
            df = pd.read_excel(filepath, engine="openpyxl")
            logger.debug(f"Загружено {len(df)} транзакций из XLSX.")
            return df.to_dict(orient="records")

        else:
            logger.error(f"Неподдерживаемый формат файла: {path.suffix}")
            raise ValueError(f"Неподдерживаемый формат файла: {path.suffix}")

    except Exception as e:
        logger.exception(f"Ошибка при загрузке файла: {e}")
        raise
