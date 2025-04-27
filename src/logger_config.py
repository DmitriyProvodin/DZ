import logging
import os


def setup_logger(name: str, filename: str) -> logging.Logger:
    """
    Настраивает и возвращает логгер с именем name, который пишет в logs/filename.
    Лог файл будет перезаписываться при каждом запуске приложения.
    """

    # Создаем папку logs, если её нет
    logs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Logs")
    os.makedirs(logs_dir, exist_ok=True)

    # Полный путь до файла лога
    log_path = os.path.join(logs_dir, filename)

    # Создаем логгер
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Очищаем предыдущие хендлеры, чтобы не плодились логи
    if logger.hasHandlers():
        logger.handlers.clear()

    # Создаем обработчик для записи в файл (перезаписывает файл при запуске)
    file_handler = logging.FileHandler(log_path, mode='w', encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)

    # Настраиваем форматтер
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(formatter)

    # Добавляем обработчик к логгеру
    logger.addHandler(file_handler)

    return logger
