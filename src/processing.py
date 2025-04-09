def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    """
    Возвращает список операций, у которых статус совпадает с переданным.
    По умолчанию фильтрует по статусу "EXECUTED".
    """
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: list, reverse: bool = True) -> list:
    """
    Сортирует список операций по дате.
    По умолчанию сортирует по убыванию (reverse=True).
    """
    return sorted(data, key=lambda x: x.get("date"), reverse=reverse)
