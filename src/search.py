import re
from typing import List, Dict

def search_by_description(transactions: List[Dict], keyword: str) -> List[Dict]:
    """
    Возвращает список транзакций, содержащих keyword в описании (description), регистронезависимо.

    :param transactions: Список транзакций.
    :param keyword: Строка поиска.
    :return: Отфильтрованный список транзакций.
    """
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    return [txn for txn in transactions if pattern.search(txn.get("description", ""))]
