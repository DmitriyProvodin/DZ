from typing import Generator, Dict


def filter_by_currency(transactions: list[Dict], currency_code: str) -> Generator[Dict, None, None]:
    """
    Генератор, фильтрующий транзакции по коду валюты.
    """
    for t in transactions:
        if t.get("operationAmount", {}).get("currency", {}).get("code") == currency_code:
            yield t


def transaction_descriptions(transactions: list[Dict]) -> Generator[str, None, None]:
    """
    Генератор описаний операций.
    """
    for t in transactions:
        yield t.get("description", "")


def card_number_generator(transactions: list[Dict]) -> Generator[str, None, None]:
    """
    Генератор, возвращающий маскированные номера карт и счетов.
    """
    for t in transactions:
        source = t.get("from") or t.get("to", "")
        yield mask_sensitive_info(source)


def mask_sensitive_info(text: str) -> str:
    """
    Маскирует номер карты или счета.
    Примеры:
        Счет 1234567890 -> Счет **7890
        Visa Classic 1234 5678 9012 3456 -> Visa Classic 1234 56** **** 3456
    """
    if "Счет" in text:
        return "Счет **" + text[-4:]
    parts = text.split()
    if len(parts) >= 2 and parts[-1].isdigit():
        number = parts[-1]
        return f"{' '.join(parts[:-1])} {number[:4]} {number[4:6]}** **** {number[-4:]}"
    return text
