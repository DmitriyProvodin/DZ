def mask_card_number(card_info: str) -> str:
    """
    Маскирует номер карты, оставляя первые 6 и последние 4 цифры.
    Пример: 'MasterCard 1234 56** **** 7890'
    """
    parts = card_info.split()
    if not parts:
        return card_info

    name = " ".join(parts[:-1])
    digits = parts[-1].replace(" ", "")

    if len(digits) < 16:
        return card_info  # некорректный формат

    return f"{name} {digits[:4]} {digits[4:6]}** **** {digits[-4:]}"


def mask_account_number(account_info: str) -> str:
    """
    Маскирует номер счета, оставляя только последние 4 цифры.
    Пример: 'Счет **1234'
    """
    if account_info.startswith("Счет"):
        return f"Счет **{account_info[-4:]}"
    return account_info
