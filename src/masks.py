import logging

# Создание логгера для модуля masks
logger = logging.getLogger("masks_logger")

# Установка уровня логирования
logger.setLevel(logging.DEBUG)

# Настройка file_handler — файл, куда будут сохраняться логи
file_handler = logging.FileHandler("masks.log", encoding="utf-8")

# Установка уровня логирования для file_handler
file_handler.setLevel(logging.DEBUG)

# Настройка форматтера — как будет выглядеть каждая строка в логе
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Привязываем форматтер к file_handler
file_handler.setFormatter(file_formatter)

# Добавляем обработчик к логгеру
logger.addHandler(file_handler)


# Пример функции с логированием
def mask_card_number(card_number: str) -> str:
    """Маскирует номер карты, оставляя видимыми только первые 6 и последние 4 цифры"""
    logger.debug(f"Начата маскировка карты: {card_number}")
    try:
        if len(card_number) < 12:
            raise ValueError("Неверный формат номера карты")

        masked = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        logger.info(f"Маскировка успешно выполнена: {masked}")
        return masked
    except Exception as e:
        logger.error(f"Ошибка при маскировке карты: {e}")
        raise
