from src.processing import filter_by_status, sort_by_date, search_by_description, display_operations
from src.generators import filter_by_currency
from src.load_transactions import load_from_json


def main() -> None:
    # Загрузка операций из файла
    file_path = "data/operations.json"
    operations = load_from_json(file_path)

    if not operations:
        print("Не удалось загрузить данные.")
        return

    while True:
        print("\n📋 Меню:")
        print("1. Показать все операции")
        print("2. Фильтровать по статусу")
        print("3. Сортировать по дате")
        print("4. Найти по описанию")
        print("5. Фильтровать по валюте")
        print("0. Выход")

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            display_operations(operations)

        elif choice == "2":
            status = input("Введите статус (например, EXECUTED): ")
            filtered = filter_by_status(operations, status)
            display_operations(filtered)

        elif choice == "3":
            sorted_ops = sort_by_date(operations)
            display_operations(sorted_ops)

        elif choice == "4":
            keyword = input("Введите ключевое слово для поиска: ")
            found = search_by_description(operations, keyword)
            display_operations(found)

        elif choice == "5":
            currency = input("Введите код валюты (например, USD, EUR, RUB): ")
            filtered = list(filter_by_currency(operations, currency))
            display_operations(filtered)

        elif choice == "0":
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор. Попробуйте снова.")
