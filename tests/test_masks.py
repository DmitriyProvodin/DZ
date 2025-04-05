import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.fixture
def right_get_mask_card_number():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


@pytest.mark.parametrize(
    "user_input, expected",
    [
        ("401288881888", "4012 88** 1888"),
        ("4012888818888", "4012 88** *888 8"),
        ("37598765432100", "3759 87**** 2100"),
        ("375987654321001", "3759 87**** *1001"),
        ("70007922896063610", "7000 79** **** *361 0"),
        ("700079228960636101", "7000 79** **** **61 01"),
        ("7000792289606361012", "7000 79** *******1 012"),
    ],
)
def len_get_mask_card_number(user_input, expected):
    assert get_mask_card_number(user_input) == expected


@pytest.fixture
def empty_get_mask_card_number():
    assert get_mask_card_number("") == "Вы ничего не указали, введите номер карты"


@pytest.mark.parametrize(
    "user_input, expected",
    [("73654108430135874305", "** 4305"), ("73654108430135854893", "** 4893")],
)
def right_get_mask_account(user_input, expected):
    assert get_mask_account(user_input) == expected


@pytest.mark.parametrize(
    "user_input, expected",
    [
        ("73654108430135854893", "** 4893"),
        ("736541084301358548931231231", "** 1231"),
        ("123123213023002", "** 3002"),
    ],
)
def len_get_mask_account(user_input, expected):
    assert get_mask_account(user_input) == expected