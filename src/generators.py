from typing import Generator, Dict


def filter_by_currency(transactions: list[dict], currency: str) -> Generator[Dict, None, None]:
    """
    Возвращает только те транзакции, в которых валюта совпадает с переданной.
    """
    for t in transactions:
        if t.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield t


def transaction_descriptions(transactions: list[dict]) -> Generator[str, None, None]:
    """
    Генератор описаний транзакций.
    """
    for t in transactions:
        yield t.get("description", "")


def card_number_generator(transactions: list[dict]) -> Generator[str, None, None]:
    """
    Генератор номеров карт из поля 'from', если они присутствуют.
    """
    for t in transactions:
        from_field = t.get("from", "")
        number = from_field.split(" ")[-1]
        if number.isdigit() and len(number) == 16:
            yield number
