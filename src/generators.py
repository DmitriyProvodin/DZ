from typing import Iterator

def filter_by_currency(data: list[dict], currency: str = "USD") -> Iterator[dict]:
    """
    Генератор, возвращающий операции в указанной валюте.
    """
    for item in data:
        if item.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield item

def transaction_descriptions(data: list[dict]) -> Iterator[str]:
    """
    Генератор, возвращающий описания операций.
    """
    for item in data:
        desc = item.get("description")
        if desc:
            yield desc

def card_number_generator(data: list[dict]) -> Iterator[str]:
    """
    Генератор, возвращающий все номера карт/счетов из 'from' и 'to'.
    """
    for item in data:
        for key in ("from", "to"):
            value = item.get(key)
            if value:
                yield value
