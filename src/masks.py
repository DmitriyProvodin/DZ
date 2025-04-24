from logger_config import setup_logger

logger = setup_logger("masks", "masks.log")

def mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты: показывает первые 6 и последние 4 цифры, остальное заменяет на '*'.
    """
    try:
        masked = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        logger.info(f"Маскирование номера карты: {card_number} -> {masked}")
        return masked
    except Exception as e:
        logger.error(f"Ошибка при маскировании номера карты: {card_number} — {e}")
        return card_number


def mask_account_number(account_number: str) -> str:
    """
    Маскирует номер счёта: показывает только последние 4 цифры, остальное заменяет на '*'.
    """
    try:
        masked = f"**{account_number[-4:]}"
        logger.info(f"Маскирование номера счёта: {account_number} -> {masked}")
        return masked
    except Exception as e:
        logger.error(f"Ошибка при маскировании номера счёта: {account_number} — {e}")
        return account_number
