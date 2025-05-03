# widget.py

from datetime import datetime

def mask_account_number(account: str) -> str:
    """
    Маскирует номер счёта: оставляет только последние 4 цифры.
    Пример: "Счет 43219876543212345678" → "Счет **5678"
    """
    parts = account.split()
    if len(parts) == 2 and parts[0].lower() == "счет":
        return f"{parts[0]} **{parts[1][-4:]}"
    return account


def mask_card_number(card: str) -> str:
    """
    Маскирует номер карты: показывает первые 6 и последние 4 цифры, остальное заменяет на ****
    Пример: "Visa Platinum 7492657788887202" → "Visa Platinum 7492 65** **** 7202"
    """
    parts = card.split()
    if len(parts) >= 2:
        name = " ".join(parts[:-1])
        number = parts[-1]
        if len(number) >= 16:
            return f"{name} {number[:4]} {number[4:6]}** **** {number[-4:]}"
    return card


def format_date(date_str: str) -> str:
    """
    Преобразует дату из ISO в формат "дд.мм.гггг"
    Пример: "2019-12-08T22:46:21.935582" → "08.12.2019"
    """
    try:
        date = datetime.fromisoformat(date_str)
        return date.strftime("%d.%m.%Y")
    except ValueError:
        return date_str
