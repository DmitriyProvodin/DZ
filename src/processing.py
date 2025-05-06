from typing import List, Dict
from collections import Counter
import re
from src.widget import format_date, get_mask_account_card


def filter_by_status(transactions: List[Dict], status: str) -> List[Dict]:
    """Фильтрация по статусу операции."""
    return [t for t in transactions if t.get("state", "").upper() == status.upper()]


def sort_by_date(transactions: List[Dict], reverse: bool = True) -> List[Dict]:
    """Сортировка по дате."""
    return sorted(transactions, key=lambda x: x.get("date", ""), reverse=reverse)


def search_by_description(transactions: List[Dict], query: str) -> List[Dict]:
    """Фильтрация транзакций по описанию через re."""
    pattern = re.compile(query, re.IGNORECASE)
    return [t for t in transactions if pattern.search(t.get("description", ""))]


def count_operations_by_category(transactions: List[Dict], categories: List[str]) -> Dict[str, int]:
    """Подсчет количества операций по категориям."""
    descriptions = [t.get("description", "") for t in transactions]
    counter = Counter()
    for category in categories:
        counter[category] = sum(1 for desc in descriptions if category.lower() in desc.lower())
    return dict(counter)


def display_operations(transactions: List[Dict]) -> None:
    """Вывод списка операций в консоль в читаемом формате."""
    print(f"\nВсего банковских операций в выборке: {len(transactions)}\n")
    for t in transactions:
        date = format_date(t.get("date", ""))
        desc = t.get("description", "")
        from_ = get_mask_account_card(t.get("from", "Не указано"))
        to_ = get_mask_account_card(t.get("to", "Не указано"))
        amount = t.get("operationAmount", {}).get("amount", 0)
        currency = t.get("operationAmount", {}).get("currency", {}).get("code", "RUB")
        print(f"{date} {desc}\n{from_} -> {to_}\nСумма: {amount} {currency}\n")
