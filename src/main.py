from processing import filter_by_status, sort_by_date
from search import search_by_description
from generators import filter_by_currency
from widget import mask_account_number, mask_card_number, format_date

def display_operations(operations: list[dict]) -> None:
    """
    Выводит список операций в требуемом формате.
    """
    for op in operations:
        # Форматируем дату
        date = format_date(op.get("date", ""))
        # Получаем описание
        description = op.get("description", "")

        # Обрабатываем поле from
        from_ = op.get("from")
        if from_:
            if "счет" in from_.lower():
                from_ = mask_account_number(from_)
            else:
                from_ = mask_card_number(from_)
        else:
            from_ = ""

        # Обрабатываем поле to
        to = op.get("to", "")
        if "счет" in to.lower():
            to = mask_account_number(to)
        else:
            to = mask_card_number(to)

        # Получаем сумму и валюту
        amount_info = op.get("operationAmount", {})
        amount = amount_info.get("amount", "")
        currency = amount_info.get("currency", {}).get("name", "")

        # Печатаем результат
        print(f"{date} {description}")
        if from_:
            print(f"{from_} -> {to}")
        else:
            print(f"{to}")
        print(f"{amount} {currency}\n")
