def filter_by_state(date_list: list, state: str = "EXECUTED") -> list:
    """Функция для фильтрации словарей в списке по заданному ключу"""
    filtered_list = [i for i in date_list if i["state"] == state]
    return filtered_list


def sort_by_date(date_list: list, vector: bool = True) -> list:
    """Функция сортировки списка словарей по дате"""
    return sorted(date_list, key=lambda i: i["date"], reverse=vector)
