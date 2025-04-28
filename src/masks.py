from logger_config import setup_logger

logger = setup_logger('masks', 'masks.log')

def mask_card_number(card_number: str) -> str:
    """Маскирует номер карты, оставляя только часть цифр видимыми."""
    logger.debug(f"Начата маскировка номера карты: {card_number}")
    try:
        if len(card_number) < 12:
            raise ValueError("Неверный формат номера карты: слишком короткий")

        masked = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        logger.info(f"Маскировка карты успешно выполнена для номера: {card_number}")
        return masked
    except Exception as error:
        logger.error(f"Ошибка при маскировке номера карты: {error}")
        raise
