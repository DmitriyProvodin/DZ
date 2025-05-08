def mask_card_number(card_str: str) -> str:
    """
    Маскирует номер карты. Пример:
    "Visa Classic 1234567812345678" → "Visa Classic 1234 56** **** 5678"
    """
    parts = card_str.rsplit(" ", 1)
    if len(parts) != 2 or not parts[1].isdigit():
        return card_str

    name, number = parts
    masked = f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
    return f"{name} {masked}"


def mask_account_number(account_str: str) -> str:
    """
    Маскирует номер счёта. Пример:
    "Счет 12345678901234567890" → "Счет **7890"
    """
    parts = account_str.rsplit(" ", 1)
    if len(parts) != 2 or not parts[1].isdigit():
        return account_str

    name, number = parts
    return f"{name} **{number[-4:]}"
