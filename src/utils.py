import logging
import json
from typing import Any

# 🔹 Создание логгера для модуля utils
logger = logging.getLogger("utils_logger")

# 🔹 Установка уровня логирования
logger.setLevel(logging.DEBUG)

# Настройка file_handler — файл, куда будут сохраняться логи
file_handler = logging.FileHandler("utils.log", encoding="utf-8")

# Установка уровня логирования для file_handler
file_handler.setLevel(logging.DEBUG)

# Настройка форматтера
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Привязка форматтера к обработчику
file_handler.setFormatter(file_formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)


# Пример функции: загрузка данных из JSON-файла
def load_json_data(file_path: str) -> Any:
    """Загружает данные из JSON-файла по указанному пути"""
    logger.debug(f"Попытка загрузить файл: {file_path}")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        logger.info(f"Файл успешно загружен: {file_path}")
        return data
    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}")
        raise
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка декодирования JSON: {e}")
        raise
    except Exception as e:
        logger.error(f"Неизвестная ошибка при загрузке файла: {e}")
        raise
