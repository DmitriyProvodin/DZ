import json
from typing import List, Dict


def load_from_json(file_path: str) -> List[Dict]:
    """
    Загружает данные из JSON-файла.
    """
    try:
        with open(file_path, encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
