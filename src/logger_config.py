import logging
import os


def setup_logger(name: str, filename: str) -> logging.Logger:
    """
    Настраивает логгер для модуля.
    """
    logs_dir = "logs"
    os.makedirs(logs_dir, exist_ok=True)
    filepath = os.path.join(logs_dir, filename)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    file_handler = logging.FileHandler(filepath, mode='w', encoding='utf-8')
    file_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(file_handler)

    return logger
