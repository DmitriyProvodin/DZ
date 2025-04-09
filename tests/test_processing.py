import pytest
from src.processing import filter_by_state, sort_by_date

# Пример данных, с которыми будем работать
data = [
    {"id": 1, "state": "EXECUTED", "date": "2022-01-10T10:00:00"},
    {"id": 2, "state": "CANCELED", "date": "2022-01-12T10:00:00"},
    {"id": 3, "state": "EXECUTED", "date": "2022-01-11T11:00:00"},
]

# Проверяем, что по умолчанию фильтруются только выполненные (EXECUTED)
def test_filter_by_state_default():
    result = filter_by_state(data)  # без указания состояния
    assert len(result) == 2  # должно быть 2 записи
    assert all(item["state"] == "EXECUTED" for item in result)  # все должны быть EXECUTED

# Проверяем фильтрацию по состоянию CANCELED
def test_filter_by_state_custom():
    result = filter_by_state(data, state="CANCELED")
    assert len(result) == 1  # одна запись
    assert result[0]["id"] == 2  # у этой записи id должен быть 2
    assert result[0]["state"] == "CANCELED"  # и состояние CANCELED

# Проверяем ситуацию, когда не найдено ни одной записи (например, по PENDING)
def test_filter_by_state_none_match():
    result = filter_by_state(data, state="PENDING")
    assert result == []  # результат — пустой список

# Проверяем сортировку по дате — от самой новой к старой
def test_sort_by_date_descending():
    result = sort_by_date(data)
    dates = [item["date"] for item in result]
    assert dates == sorted(dates, reverse=True)  # список должен быть отсортирован от новой даты к старой

# Проверяем сортировку по дате — от самой старой к новой
def test_sort_by_date_ascending():
    result = sort_by_date(data, reverse=False)
    dates = [item["date"] for item in result]
    assert dates == sorted(dates)  # список должен быть отсортирован от старой даты к новой
