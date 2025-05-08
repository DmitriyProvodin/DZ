import pytest
import pandas as pd
from unittest.mock import mock_open, patch

from src.load_transactions import load_transactions


@pytest.fixture
def fake_json_data() -> str:
    return '[{"id": 1, "amount": 1000, "currency": "RUB"}]'


def test_load_json_transactions(fake_json_data: str) -> None:
    with patch("builtins.open", mock_open(read_data=fake_json_data)):
        with patch("pathlib.Path.exists", return_value=True):
            result = load_transactions("data/transactions.json")
            assert isinstance(result, list)
            assert result[0]["amount"] == 1000


def test_load_csv_transactions() -> None:
    data = "id,amount,currency\n1,1000,RUB\n"
    with patch("pandas.read_csv", return_value=pd.DataFrame([{"id": 1, "amount": 1000, "currency": "RUB"}])):
        with patch("pathlib.Path.exists", return_value=True):
            result = load_transactions("data/transactions.csv")
            assert isinstance(result, list)
            assert result[0]["currency"] == "RUB"


def test_load_xlsx_transactions() -> None:
    with patch("pandas.read_excel", return_value=pd.DataFrame([{"id": 1, "amount": 1000, "currency": "RUB"}])):
        with patch("pathlib.Path.exists", return_value=True):
            result = load_transactions("data/transactions.xlsx")
            assert isinstance(result, list)
            assert result[0]["id"] == 1
