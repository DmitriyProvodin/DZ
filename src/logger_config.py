import logging
import os

def setup_logger(name: str, filename: str) -> logging.Logger:
    """Настраивает и возвращает логгер для модуля."""
    # Путь к папке logs
    logs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Logs')
    os.makedirs(logs_dir, exist_ok=True)

    # Полный путь к файлу лога
    log_path = os.path.join(logs_dir, filename)

    # Создаем логгер
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Убираем старые хендлеры, чтобы не было дублирования
    if logger.hasHandlers():
        logger.handlers.clear()

    # Создаем обработчик для записи в файл
    file_handler = logging.FileHandler(log_path, mode='w', encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)

    # Формат логов
    formatter = logging.Formatter(
        fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(formatter)

    # Добавляем обработчик к логгеру
    logger.addHandler(file_handler)

    return logger
