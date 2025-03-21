from file_classes import ФайлJson, ФайлTxt, ФайлCsv

def тест_json_файла():
    json_файл = ФайлJson("тест.json")
    # Тест записи
    данные = {"имя": "Никита", "курс": "Python"}
    json_файл.записать(данные)
    
    # Тест чтения
    прочитанные_данные = json_файл.читать()
    print("Чтение JSON:", прочитанные_данные)
    
    # Тест добавления
    новые_данные = {"оценка": "отлично"}
    json_файл.добавить(новые_данные)
    print("JSON после добавления:", json_файл.читать())

def тест_txt_файла():
    txt_файл = ФайлTxt("тест.txt")
    # Тест записи
    txt_файл.записать("Привет! Это тестовый файл.\n")
    
    # Тест чтения
    содержимое = txt_файл.читать()
    print("Чтение TXT:", содержимое)
    
    # Тест добавления
    txt_файл.добавить("Добавляем новую строку!\n")
    print("TXT после добавления:", txt_файл.читать())

def тест_csv_файла():
    csv_файл = ФайлCsv("тест.csv")
    # Тест записи
    данные = [
        ["Имя", "Возраст", "Город"],
        ["Никита", "26", "Чита"]
    ]
    csv_файл.записать(данные)
    
    # Тест чтения
    содержимое = csv_файл.читать()
    print("Чтение CSV:", содержимое)
    
    # Тест добавления
    новые_данные = [["Роза", "25", "Тула"]]
    csv_файл.добавить(новые_данные)
    print("CSV после добавления:", csv_файл.читать())

if __name__ == "__main__":
    print("Тестирование операций с JSON файлом:")
    тест_json_файла()
    print("\nТестирование операций с TXT файлом:")
    тест_txt_файла()
    print("\nТестирование операций с CSV файлом:")
    тест_csv_файла()
