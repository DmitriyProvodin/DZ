import pytest
from src.generators import transaction_descriptions

@pytest.fixture
def data_transaction_descriptions():
    """Тестовые данные для функции transaction_descriptions"""
    return []

@pytest.fixture
def data_transaction_descriptions_2():
    """Ожидаемый результат теста функции transaction_descriptions"""
    return ["Ошибка! Список транзакций отстутствует"]

@pytest.mark.parametrize("waiting, result", [("data_transaction_descriptions", "data_transaction_descriptions_2")])

def test_transaction_descriptions_2(waiting, result, request):
    waiting_data = request.getfixturevalue(waiting)
    result_data = request.getfixturevalue(result)
    assert list(transaction_descriptions(waiting_data)) == result_data