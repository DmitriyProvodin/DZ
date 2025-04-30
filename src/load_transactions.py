import pandas as pd


def load_csv_transactions(filepath: str) -> list[dict]:
    """
    Загружает финансовые транзакции из CSV-файла.

    :param filepath: Путь к CSV-файлу.
    :return: Список словарей с транзакциями.
    """
    df = pd.read_csv(filepath)
    return df.to_dict(orient="records")


def load_excel_transactions(filepath: str) -> list[dict]:
    """
    Загружает финансовые транзакции из Excel-файла.

    :param filepath: Путь к Excel-файлу.
    :return: Список словарей с транзакциями.
    """
    df = pd.read_excel(filepath)
    return df.to_dict(orient="records")


if __name__ == "__main__":
    # Проверочный запуск
    csv_data = load_csv_transactions("Data/transactions.csv")
    print("CSV:", csv_data)

    excel_data = load_excel_transactions("Data/transactions_excel.xlsx")
    print("Excel:", excel_data)
