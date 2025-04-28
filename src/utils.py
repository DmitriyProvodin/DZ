import json
from logger_config import setup_logger

logger = setup_logger('utils', 'utils.log')

def load_operations(file_path: str) -> list:
    """Загружает список операций из JSON-файла."""
    logger.debug(f"Попытка загрузить файл: {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            operations = json.load(file)
        logger.info(f"Файл {file_path} успешно загружен.")
        return operations
    except FileNotFoundError as error:
        logger.error(f"Файл {file_path} не найден: {error}")
        raise
    except json.JSONDecodeError as error:
        logger.error(f"Ошибка декодирования JSON в файле {file_path}: {error}")
        raise
    except Exception as error:
        logger.error(f"Неизвестная ошибка при загрузке файла {file_path}: {error}")
        raise
