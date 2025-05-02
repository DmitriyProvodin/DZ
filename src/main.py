import re
from collections import Counter
from typing import List, Dict

from src.utils import load_json_data
from src.load_transactions import load_csv_transactions, load_excel_transactions


def search_by_description(transactions: List[Dict], query: str) -> List[Dict]:
    """Фильтрация транзакций по описанию через re."""
    pattern = re.compile(query, re.IGNORECASE)
    return [t for t in transactions if pattern.search(t.get("description", ""))]


def count_operations_by_category(transactions: List[Dict], categories: List[str]) -> Dict[str, int]:
    """Подсчет количества операций по категориям."""
    descriptions = [t.get("description", "") for t in transactions]
    counter = Counter()
    for category in categories:
        counter[category] = sum(1 for desc in descriptions if category.lower() in desc.lower())
    return dict(counter)


def filter_by_status(transactions: List[Dict], status: str) -> List[Dict]:
    """Фильтрация по статусу операции."""
    return [t for t in transactions if t.get("state", "").upper() == status.upper()]


def main():
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

    if input("Отсортировать операции по дате? Да/Нет: ").lower() == "да":
        reverse = input("Отсортировать по возрастанию или по убыванию? ").lower() != "по возрастанию"
        transactions.sort(key=lambda x: x.get("date", ""), reverse=reverse)

    if input("Выводить только рублевые транзакции? Да/Нет: ").lower() == "да":
        transactions = [t for t in transactions if t.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"]

    if input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").lower() == "да":
        keyword = input("Введите слово для поиска: ")
        transactions = search_by_description(transactions, keyword)

    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    if input("Хотите посчитать количество операций по категориям? Да/Нет: ").lower() == "да":
        categories = ["оплата", "перевод", "снятие", "зачисление"]  # Пример категорий
        counts = count_operations_by_category(transactions, categories)
        print("\nКоличество операций по категориям:")
        for category, count in counts.items():
            print(f"{category}: {count}")

    print("\nРаспечатываю итоговый список транзакций...")
    print(f"\nВсего банковских операций в выборке: {len(transactions)}\n")

    for t in transactions:
        date = t.get("date", "")[:10]
        desc = t.get("description", "")
        from_ = t.get("from", "Не указано")
        to_ = t.get("to", "Не указано")
        amount = t.get("operationAmount", {}).get("amount", 0)
        currency = t.get("operationAmount", {}).get("currency", {}).get("code", "RUB")
        print(f"{date} {desc}\n{from_} -> {to_}\nСумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()
