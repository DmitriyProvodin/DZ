from typing import List, Dict


def filter_by_status(transactions: List[Dict], status: str) -> List[Dict]:
    """
    Возвращает список операций с указанным статусом.
    """
    return [t for t in transactions if t.get("state") == status]


def sort_by_date(transactions: List[Dict]) -> List[Dict]:
    """
    Сортирует список операций по дате в порядке убывания.
    """
    return sorted(transactions, key=lambda x: x.get("date", ""), reverse=True)
