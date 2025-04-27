from logger_config import setup_logger

# Настроим логгер
logger = setup_logger(name="masks", filename="masks.log")


def mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты, оставляя только первые 6 и последние 4 цифры.
    """
    logger.debug(f"Начата маскировка номера карты: {card_number}")

    if len(card_number) < 10:
        logger.error(f"Некорректный номер карты для маскировки: {card_number}")
        return card_number

    masked = f"{card_number[:6]}{'*' * (len(card_number) - 10)}{card_number[-4:]}"
    logger.info(f"Успешно замаскирован номер карты")
    return masked


def mask_account_number(account_number: str) -> str:
    """
    Маскирует номер счёта, оставляя только последние 4 цифры.
    """
    logger.debug(f"Начата маскировка номера счёта: {account_number}")

    if len(account_number) < 4:
        logger.error(f"Некорректный номер счёта для маскировки: {account_number}")
        return account_number

    masked = f"**{account_number[-4:]}"
    logger.info(f"Успешно замаскирован номер счёта")
    return masked
