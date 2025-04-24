import json
import os
from typing import Any
from logger_config import setup_logger

logger = setup_logger("utils", "utils.log")


def load_transactions(path: str) -> list[dict[str, Any]]:
    """
    Загружает список транзакций из JSON-файла.
    Возвращает пустой список, если файл не найден, пустой или содержит не список.
    """
    try:
        if not os.path.exists(path):
            logger.warning(f"Файл не найден: {path}")
            return []

        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            logger.warning(f"Ожидался список, но получено: {type(data)}")
            return []

        logger.info(f"Успешно загружено {len(data)} транзакций из {path}")
        return data

    except json.JSONDecodeError as e:
        logger.error(f"Ошибка при чтении JSON из файла {path}: {e}")
        return []
    except Exception as e:
        logger.error(f"Неожиданная ошибка при загрузке транзакций из {path}: {e}")
        return []
