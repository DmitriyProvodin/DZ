import pytest
from src.widget import mask_account_card

# Проверка: корректный номер карты
def test_mask_account_card_valid_card():
    data = "Visa 1234567812345678"
    result = mask_account_card(data)
    assert result == "Visa 1234 56** **** 5678"  # маскируем средние цифры

# Проверка: корректный номер счёта
def test_mask_account_card_valid_account():
    data = "Счет 12345678901234567890"
    result = mask_account_card(data)
    assert result == "Счет **7890"  # показываем только последние 4 цифры

# Проверка: только текст, без номера
def test_mask_account_card_invalid_format_only_text():
    data = "Просто текст без номера"
    result = mask_account_card(data)
    assert result == "Неверный формат данных"  # формат неправильный

# Проверка: номер карты слишком короткий
def test_mask_account_card_invalid_length_card():
    data = "Visa 12345678"
    result = mask_account_card(data)
    assert result == "Неверный формат данных"  # недостаточно цифр

# Проверка: номер счёта слишком короткий
def test_mask_account_card_invalid_length_account():
    data = "Счет 12345678"
    result = mask_account_card(data)
    assert result == "Неверный формат данных"  # тоже короткий

# Проверка: передана пустая строка
def test_mask_account_card_empty_string():
    data = ""
    result = mask_account_card(data)
    assert result == "Неверный формат данных"

# Проверка: отсутствует номер (только Visa)
def test_mask_account_card_missing_number():
    data = "Visa"
    result = mask_account_card(data)
    assert result == "Неверный формат данных"

# Проверка: номер содержит буквы
def test_mask_account_card_non_digit_number():
    data = "Visa 1234ABCD5678FGH1"
    result = mask_account_card(data)
    assert result == "Неверный формат данных"
