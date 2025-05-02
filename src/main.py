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
        pattern = re.compile(category, re.IGNORECASE)
        counter[category] = sum(1 for desc in descriptions if pattern.search(desc))
    return dict(counter)


def filter_by_status(transactions: List[Dict], status: str) -> List[Dict]:
    """Фильтрация по статусу операции."""
    return [t for t in transactions if t.get("state", "").upper() == status.upper()]


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
          "Выберите источник данных:\n"
          "1. JSON-файл\n2. CSV-файл\n3. XLSX-файл")

    choice = input("Ваш выбор: ").strip()
    if choice == "1":
        transactions = load_json_data("data/operations.json")
    elif choice == "2":
        transactions = load_csv_transactions("data/transactions.csv")
    elif choice == "3":
        transactions = load_excel_transactions("data/transactions.xlsx")
    else:
        print("Неверный выбор. Завершение работы.")
        return

    status = input("Введите статус (EXECUTED, CANCELED, PENDING): ").strip().upper()
    transactions = filter_by_status(transactions, status)

    if not transactions:
        print("Нет транзакций с таким статусом.")
        return

    if input("Отсортировать по дате? (Да/Нет): ").strip().lower() == "да":
        reverse = input("Сортировка по убыванию? (Да/Нет): ").strip().lower() == "да"
        transactions.sort(key=lambda x: x.get("date", ""), reverse=reverse)

    if input("Фильтровать только рублевые? (Да/Нет): ").strip().lower() == "да":
        transactions = [
            t for t in transactions
            if t.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"
        ]

    if input("Поиск по описанию? (Да/Нет): ").strip().lower() == "да":
        keyword = input("Введите слово или шаблон для поиска: ").strip()
        transactions = search_by_description(transactions, keyword)

    if not transactions:
        print("Ничего не найдено по заданным условиям.")
        return

    if input("Подсчитать количество операций по категориям? (Да/Нет): ").strip().lower() == "да":
        category_input = input("Введите категории через запятую: ").strip()
        categories = [c.strip() for c in category_input.split(",")]
        category_counts = count_operations_by_category(transactions, categories)
        print("\nОперации по категориям:")
        for cat, count in category_counts.items():
            print(f"{cat}: {count}")

    print("\nСписок транзакций:")
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
