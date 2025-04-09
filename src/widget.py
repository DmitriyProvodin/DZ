from src.masks import get_mask_card_number, get_mask_account

def mask_account_card(data: str) -> str:
    """
    Маскирует номер карты или счета в строке
    """
    parts = data.split()
    if not parts:
        return "Неверный формат данных"

    # Последнее значение — номер
    number = parts[-1]
    name = " ".join(parts[:-1])  # Всё, что до номера — имя карты/типа

    if number.isdigit() and len(number) == 16:
        # Карта
        masked = get_mask_card_number(number)
        return f"{name} {masked}"
    elif number.isdigit() and len(number) == 20:
        # Счёт
        masked = get_mask_account(number)
        return f"{name} {masked}"
    else:
        return "Неверный формат данных"
