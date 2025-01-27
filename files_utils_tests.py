
from files_utils import *

test_json_data = [
    {"имя": "Иван", "возраст": 30},
    {"имя": "Мария", "возраст": 25}
]

test_csv_data = [
    {"имя": "Иван", "город": "Москва", "возраст": "30"},
    {"имя": "Мария", "город": "Санкт-Петербург", "возраст": "25"}
]

# Тестирование JSON функций
write_json(*test_json_data, file_path="test.json")
print("Тест чтения JSON:", read_json("test.json"))
