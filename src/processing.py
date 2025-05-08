from typing import List, Dict
from src.widget import get_mask_account_card, format_date


def filter_by_status(transactions: List[Dict], status: str) -> List[Dict]:
    """
    Фильтрует список транзакций по указанному статусу.
    """
    return [t for t in transactions if t.get("state") == status]


def sort_by_date(transactions: List[Dict], ascending: bool=True) -> List[Dict]:
    """
    Сортирует список транзакций по дате (от новых к старым).
    """
    return sorted(
        transactions,
        key=lambda t: t.get("date", ""),
        reverse=ascending
    )


def search_by_description(transactions: List[Dict], keyword: str) -> List[Dict]:
    """
    Ищет транзакции по ключевому слову в описании операции.
    """
    return [t for t in transactions if keyword.lower() in t.get("description", "").lower()]


def display_operations(transactions: List[Dict]) -> None:
    """
    Вывод списка операций в консоль в читаемом формате.
    """
    print(f"\nВсего банковских операций в выборке: {len(transactions)}\n")
    for t in transactions:
        date = format_date(t.get("date", ""))
        desc = t.get("description", "")
        from_ = get_mask_account_card(t.get("from", "Не указано"))
        to_ = get_mask_account_card(t.get("to", "Не указано"))
        amount = t.get("operationAmount", {}).get("amount", 0)
        currency = t.get("operationAmount", {}).get("currency", {}).get("code", "RUB")
        print(f"{date} {desc}\n{from_} -> {to_}\nСумма: {amount} {currency}\n")
