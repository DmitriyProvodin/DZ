import json
import os
from typing import List, Dict, Any

def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает список транзакций из JSON-файла.

    :param file_path: путь до JSON-файла
    :return: список словарей с транзакциями или пустой список
    """
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, IOError):
        return []
