import logging
import os

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Хранит уже созданные логгеры, чтобы не дублировать хендлеры
_loggers: dict[str, logging.Logger] = {}

def setup_logger(name: str, log_file: str) -> logging.Logger:
    if name in _loggers:
        return _loggers[name]

    log_path = os.path.join(LOG_DIR, log_file)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Очищаем старые хендлеры, если перезапускается
    logger.handlers.clear()

    # Перезапись файла при каждом запуске
    file_handler = logging.FileHandler(log_path, mode='w', encoding='utf-8')
    formatter = logging.Formatter(
        fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    _loggers[name] = logger
    return logger
