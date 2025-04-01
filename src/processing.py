from typing import Dict, List


def filter_by_state(info_list: List[Dict],
                    state: str = 'EXECUTED') -> List[Dict]:
    """Функция для фильтрации словарей в списке по заданному ключу"""
    return [item for item in info_list if item.get("state") == state]


def sort_by_date(info_list: List[Dict], reverse: bool = True) -> List[Dict]:
    """Функция сортировки списка словарей по дате"""
    return sorted(info_list, key=lambda x: x["date"], reverse=True)