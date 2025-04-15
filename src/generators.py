from typing import Iterator, Dict, List


# Генератор транзакций по заданной валюте
def filter_by_currency(transactions: List[Dict], currency_code: str) -> Iterator[Dict]:
    """
    Фильтрует список транзакций по нужной валюте (например, USD)
    Возвращает итератор подходящих транзакций
    """
    for transaction in transactions:
        if (
            "operationAmount" in transaction
            and "currency" in transaction["operationAmount"]
            and transaction["operationAmount"]["currency"].get("code") == currency_code
        ):
            yield transaction


# Генератор описаний транзакций
def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Генератор, который по одному выдает описания операций из списка транзакций
    """
    for transaction in transactions:
        if "description" in transaction:
            yield transaction["description"]


# Генератор номеров карт
def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генератор, выдающий номера карт от start до end включительно
    Формат номера: XXXX XXXX XXXX XXXX
    """
    for number in range(start, end + 1):
        yield f"{number:016d}"[:4] + " " + f"{number:016d}"[4:8] + " " + f"{number:016d}"[8:12] + " " + f"{number:016d}"[12:]
