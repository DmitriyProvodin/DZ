import pytest
from src import masks

@pytest.mark.parametrize("card_number, expected", [
    ("1234567812345678", "1234 56** **** 5678"),
    (1234567812345678, "1234 56** **** 5678"),
    ("1234", "Вы ввели некорректные данные!"),
    ("1234abcd5678efgh", "Вы ввели некорректные данные!"),
    ("", "Вы ввели некорректные данные!"),
])
def test_get_mask_card_number(card_number, expected):
    assert masks.get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("account_number, expected", [
    ("00000000000000004321", "**4321"),
    (98765432101234567890, "**7890"),
    ("00004321", "Вы ввели некорректные данные!"),
    ("abcdefg1234567890abcd", "Вы ввели некорректные данные!"),
    ("", "Вы ввели некорректные данные!"),
])
def test_get_mask_account(account_number, expected):
    assert masks.get_mask_account(account_number) == expected
