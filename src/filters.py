import re
from collections import Counter
from typing import List, Dict


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


def filter_by_status(transactions: List[Dict], status: str) -> List[Dict]:
    """Фильтрация по статусу операции."""
    return [t for t in transactions if t.get("state", "").upper() == status.upper()]


def filter_by_currency(transactions: List[Dict], currency_code: str) -> List[Dict]:
    """Фильтрация по коду валюты."""
    return [
        t for t in transactions
        if t.get("operationAmount", {}).get("currency", {}).get("code") == currency_code
    ]