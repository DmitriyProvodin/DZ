from datetime import datetime
from src.masks import mask_account_number, mask_card_number


def get_mask_account_card(card_or_account: str) -> str:
    number = card_or_account.split(" ")[-1]
    if number.isdigit():
        if len(number) == 16:
            return mask_card_number(card_or_account)
        else:
            return mask_account_number(card_or_account)
    else:
        return card_or_account


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
