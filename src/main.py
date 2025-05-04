from src.utils import load_json_data
from src.load_transactions import load_csv_transactions, load_excel_transactions
from src.processing import filter_by_status, filter_rub_only, sort_transactions_by_date
from src.generators import search_by_description
from src.output import display_operations


def main() -> None:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
          "Выберите необходимый пункт меню:\n"
          "1. Получить информацию о транзакциях из JSON-файла\n"
          "2. Получить информацию о транзакциях из CSV-файла\n"
          "3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Ваш выбор: ").strip()
    if choice == "1":
        transactions = load_json_data("data/operations.json")
        print("Для обработки выбран JSON-файл.")
    elif choice == "2":
        transactions = load_csv_transactions("data/transactions.csv")
        print("Для обработки выбран CSV-файл.")
    elif choice == "3":
        transactions = load_excel_transactions("data/transactions_excel.xlsx")
        print("Для обработки выбран XLSX-файл.")
    else:
        print("Неверный выбор. Завершение работы.")
        return

    # Фильтрация по статусу
    while True:
        status = input("Введите статус, по которому необходимо выполнить фильтрацию "
                       "(EXECUTED, CANCELED, PENDING): ").upper()
        if status in ["EXECUTED", "CANCELED", "PENDING"]:
            transactions = filter_by_status(transactions, status)
            print(f'Операции отфильтрованы по статусу "{status}"')
            break
        else:
            print(f'Статус операции "{status}" недоступен.')

    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    # Сортировка по дате
    if input("Отсортировать операции по дате? Да/Нет: ").strip().lower() == "да":
        order = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
        reverse = order != "по возрастанию"
        transactions = sort_transactions_by_date(transactions, reverse=reverse)

    # Только рублевые
    if input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower() == "да":
        transactions = filter_rub_only(transactions)

    # Поиск по описанию
    if input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower() == "да":
        keyword = input("Введите слово для поиска: ").strip()
        transactions = search_by_description(transactions, keyword)

    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    # Финальный вывод
    print("\nРаспечатываю итоговый список транзакций...")
    display_operations(transactions)


if __name__ == "__main__":
    main()
