
import json
import csv
import yaml
from typing import List, Dict, Any, Union, Optional

def read_json(file_path: str, encoding: str = "utf-8") -> Union[Dict, List]:
    """
    Чтение данных из JSON файла
    """
    with open(file_path, 'r', encoding=encoding) as file:
        return json.load(file)

def write_json(*data: Dict, file_path: str, encoding: str = "utf-8") -> None:
    """
    Запись данных в JSON файл
    """
    with open(file_path, 'w', encoding=encoding) as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def read_csv(file_path: str, delimiter: str = ';', encoding: str = 'utf-8-sig') -> List[Dict]:
    """
    Чтение данных из CSV файла
    """
    with open(file_path, 'r', encoding=encoding) as file:
        return list(csv.DictReader(file, delimiter=delimiter))

def read_txt(file_path: str, encoding: str = "utf-8") -> str:
    """
    Чтение данных из текстового файла
    """
    with open(file_path, 'r', encoding=encoding) as file:
        return file.read()

def append_json(*data: Dict, file_path: str, encoding: str = "utf-8") -> None:
    """
    Добавление данных в существующий JSON файл
    
    Аргументы:
        *data: Произвольное количество словарей для добавления
        file_path: Путь к JSON файлу
        encoding: Кодировка файла (по умолчанию: utf-8)
    """
    try:
        existing_data = read_json(file_path, encoding)
    except FileNotFoundError:
        existing_data = []
    
    if isinstance(existing_data, dict):
        existing_data = [existing_data]
    
    existing_data.extend(data)
    write_json(*existing_data, file_path=file_path, encoding=encoding)
