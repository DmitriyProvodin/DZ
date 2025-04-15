import pytest
from typing import List, Dict
from generators import filter_by_currency, transaction_descriptions, card_number_generator

# Пример списка транзакций
transactions: List[Dict] = [
    {
        "id": 1,
        "state": "EXECUTED",
        "date": "2023-01-01T12:00:00.000000",
        "operationAmount": {
            "amount": "100.00",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 11111111111111111111",
        "to": "Счет 22222222222222222222"
    },
    {
        "id": 2,
        "state": "EXECUTED",
        "date": "2023-01-02T12:00:00.000000",
        "operationAmount": {
            "amount": "200.00",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Оплата услуг",
        "from": "Счет 33333333333333333333",
        "to": "Счет 44444444444444444444"
    },
    {
        "id": 3,
        "state": "EXECUTED",
        "date": "2023-01-03T12:00:00.000000",
        "operationAmount": {
            "amount": "300.00",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Покупка",
        "from": "Счет 55555555555555555555",
        "to": "Счет 66666666666666666666"
    }
]

# Тест: фильтрация по валюте USD
def test_filter_by_currency_usd() -> None:
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 3

# Тест: фильтрация по валюте, которой нет
def test_filter_by_currency_not_found() -> None:
    result = list(filter_by_currency(transactions, "EUR"))
    assert result == []

# Тест: фильтрация пустого списка
def test_filter_by_currency_empty_list() -> None:
    result = list(filter_by_currency([], "USD"))
    assert result == []

# Тест: генерация описаний транзакций
def test_transaction_descriptions() -> None:
    gen = transaction_descriptions(transactions)
    assert next(gen) == "Перевод организации"
    assert next(gen) == "Оплата услуг"
    assert next(gen) == "Покупка"

# Тест: генерация описаний из пустого списка
def test_transaction_descriptions_empty() -> None:
    gen = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(gen)

# Тест: генерация номеров карт в диапазоне
def test_card_number_generator_range() -> None:
    gen = list(card_number_generator(1, 3))
    assert gen == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003"
    ]

# Тест: генерация одного номера карты
def test_card_number_generator_single() -> None:
    gen = list(card_number_generator(1234567890123456, 1234567890123456))
    assert gen == ["1234 5678 9012 3456"]

# Тест: генерация при начальном > конечного — пусто
def test_card_number_generator_invalid_range() -> None:
    gen = list(card_number_generator(5, 1))
    assert gen == []
