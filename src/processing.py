from typing import List, Dict


def sort_by_date(transactions: List[Dict], ascending: bool = False) -> List[Dict]:
    """
    Сортировка транзакций по дате.
    """
    return sorted(transactions, key=lambda t: t.get("date", ""), reverse=not ascending)


def filter_by_currency(transactions: List[Dict], currency_code: str = "RUB") -> List[Dict]:
    """
    Фильтрация транзакций по коду валюты (по умолчанию: RUB).
    """
    return [
        t for t in transactions
        if t.get("operationAmount", {}).get("currency", {}).get("code") == currency_code
    ]


def display_operations(transactions: List[Dict]) -> None:
    """
    Вывод списка операций в консоль в читаемом формате.
    """
    print(f"\nВсего банковских операций в выборке: {len(transactions)}\n")
    for t in transactions:
        date = t.get("date", "")[:10]
        desc = t.get("description", "")
        from_ = t.get("from", "Не указано")
        to_ = t.get("to", "Не указано")
        amount = t.get("operationAmount", {}).get("amount", 0)
        currency = t.get("operationAmount", {}).get("currency", {}).get("code", "RUB")
        print(f"{date} {desc}\n{from_} -> {to_}\nСумма: {amount} {currency}\n")
