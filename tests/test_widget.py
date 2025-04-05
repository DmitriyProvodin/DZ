import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "user_input, expected",
    [
        ("Счет 8432014830921482302394", "Счет **2394"),
        ("Visa Platinum 2131231284932299", "Visa Platinum 213123******2299"),
    ],
)
def test_mask_account_card(user_input, expected):
    assert mask_account_card(user_input) == expected


@pytest.mark.parametrize(
    "user_input, expected",
    [
        ("Maestro 7000792289606361", "Maestro 700079******6361"),
        ("Visa 7000792289606361", "Visa 700079******6361"),
        ("Mir 7289094321672902", "Mir 728909******2902"),
        ("Счет 8432014830921482304", "Счет **2304"),
    ],
)
def uni_mask_account_card(user_input, expected):
    assert mask_account_card(user_input) == expected


@pytest.mark.parametrize(
    "user_input, expected",
    [
        ("2.02", "Введите номер карты или счет"),
        ("Счет 1", "Введите номер карты или счет"),
        ("", "Введите номер карты или счет"),
    ],
)
def empty_mask_account_card(user_input, expected):
    assert mask_account_card(user_input) == expected


@pytest.fixture
def right_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


@pytest.fixture
def test_get_date():
    assert get_date("") == "Нет данных о дате"
