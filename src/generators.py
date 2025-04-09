# Функция-фильтр по валюте
def filter_by_currency(transactions, currency_code):
    """
    Фильтруем список транзакций по нужной валюте (например, USD)
    Возвращаем итератор подходящих транзакций.
    """
    result = []  # Создаем пустой список для результата

    for transaction in transactions:  # Проходимся по каждой транзакции
        # Проверяем, есть ли нужные ключи
        if "operationAmount" in transaction and "currency" in transaction["operationAmount"]:
            code = transaction["operationAmount"]["currency"].get("code")

            # Если код совпадает, добавляем в результат
            if code == currency_code:
                result.append(transaction)

    return iter(result)  # Возвращаем результат как итератор


# Генератор описаний транзакций
def transaction_descriptions(transactions):
    """
    Генератор, который по одному выдает описания операций из списка транзакций.
    """
    for transaction in transactions:  # Перебираем транзакции
        if "description" in transaction:  # Если есть описание
            yield transaction["description"]  # Отправляем его наружу
        else:
            yield "Описание отсутствует"  # Если нет — заглушка


# Генератор номеров карт
def card_number_generator(start, end):
    """
    Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX.
    Диапазон задается от start до end (включительно).
    """
    for number in range(start, end + 1):  # Перебираем от начального до конечного
        # Преобразуем число в строку из 16 цифр с нулями слева
        card_number = str(number).zfill(16)

        # Разбиваем по 4 цифры с пробелами
        formatted = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"

        yield formatted  # Отдаем строку наружу
