from typing import Iterator

def filter_by_status(data: list[dict], status: str = "EXECUTED") -> Iterator[dict]:
    """
    Возвращает только те операции, у которых заданный статус.
    """
    for item in data:
        if item.get("state") == status:
            yield item

def sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]:
    """
    Сортирует операции по дате.
    """
    return sorted(
        [item for item in data if "date" in item],
        key=lambda x: x["date"],
        reverse=reverse
    )
