from src.utils import load_json_data
from src.load_transactions import load_csv_transactions, load_excel_transactions
from src.filters import filter_by_status, search_by_description, filter_by_currency
from src.processing import sort_by_date, display_operations

def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
          "Выберите необходимый пункт меню:\n"
          "1. Загрузить транзакции из JSON-файла\n"
          "2. Загрузить транзакции из CSV-файла\n"
          "3. Загрузить транзакции из XLSX-файла")


    choice = input("Ваш выбор: ").strip()
    if choice == "1":
        transactions = load_json_data("Data/operations.json")
        print("Загружен JSON-файл.")
    elif choice == "2":
        transactions = load_csv_transactions("data/transactions.csv")
        print("Загружен CSV-файл.")
    elif choice == "3":
        transactions = load_excel_transactions("data/transactions_excel.xlsx")
        print("Загружен XLSX-файл.")
    else:
        print("Неверный выбор. Завершение работы.")
        return


    # Фильтрация по статусу
    while True:
        status = input("Введите статус транзакций для фильтрации (EXECUTED, CANCELED, PENDING): ").upper()
        if status in ["EXECUTED", "CANCELED", "PENDING"]:
            transactions = filter_by_status(transactions, status)


            break
        else:
            print("Некорректный статус. Попробуйте снова.")


    if not transactions:
        print("Нет транзакций с таким статусом.")
        return


    # Сортировка по дате
    if input("Отсортировать транзакции по дате? Да/Нет: ").lower() == "да":
        order = input("Сортировать по возрастанию? Да/Нет: ").lower() == "да"
        transactions = sort_by_date(transactions, ascending=order)


    # Фильтрация по валюте
    if input("Оставить только рублевые транзакции? Да/Нет: ").lower() == "да":
        transactions = filter_by_currency(transactions, "RUB")


    # Поиск по описанию
    if input("Фильтровать по ключевому слову в описании? Да/Нет: ").lower() == "да":
        keyword = input("Введите слово для поиска: ")
        transactions = search_by_description(transactions, keyword)


    if not transactions:
        print("Нет транзакций, подходящих под условия.")
        return


    # Вывод результата
    display_operations(transactions)



if __name__ == "__main__":
    main()