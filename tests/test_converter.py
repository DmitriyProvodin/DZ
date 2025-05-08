import pytest
from external_api.converter import convert_to_rub
from unittest.mock import patch


# Валюта — рубли, API не вызывается
def test_convert_to_rub_rub_currency():
    transaction = {
        "operationAmount": {
            "amount": "500.0",
            "currency": {"code": "RUB"}
        }
    }

    result = convert_to_rub(transaction)
    assert result == 500.0


# Валюта — USD, mock запроса к API
@patch("external_api.converter.requests.get")
def test_convert_to_rub_usd_currency(mock_get):
    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {"code": "USD"}
        }
    }

    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {"rates": {"RUB": 95.0}}

    result = convert_to_rub(transaction)
    assert result == 9500.0  # 100 * 95.0


# Ошибка при запросе — должен вернуть 0.0
@patch("external_api.converter.requests.get", side_effect=Exception("API error"))
def test_convert_to_rub_api_exception(mock_get):
    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {"code": "EUR"}
        }
    }

    result = convert_to_rub(transaction)
    assert result == 0.0
