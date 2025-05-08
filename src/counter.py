from collections import Counter
from typing import List, Dict

def count_by_category(transactions: List[Dict]) -> Dict[str, int]:
    """
    Подсчитывает количество транзакций по категориям из поля description.

    :param transactions: Список транзакций.
    :return: Словарь с категориями и количеством.
    """
    descriptions = [txn.get("description", "") for txn in transactions]
    return dict(Counter(descriptions))
