# Домашнее задание №15: Конвертация времени и температуры
"""
Python_Homework_2

"""
# Выбор задачи
print("Домашнее задание №15: Конвертация времени и температуры")
print("1. Конвертация секунд")
print("2. Конвертация температуры")

# Преобразование ввода, заменяя запятую на точку
task = int(str(input("Выберите задачу (1 или 2): ")).replace(',', '.').split('.')[0])

# Задача 1: Конвертация секунд
if task == 1:
    # Преобразование ввода секунд, заменяя запятую на точку
    total_seconds = int(str(input("Введите количество секунд: ")).replace(',', '.').split('.')[0])
    
    # Вычисление часов, минут и секунд
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    
    # Вывод результата с использованием одного print()
    print(f"В указанном количестве секунд ({total_seconds}):\nЧасов: {hours}\nМинут: {minutes}\nСекунд: {seconds}")

# Задача 2: Конвертация температуры
elif task == 2:
    # Замена запятой на точку для корректного преобразования
    celsius = float(input("Введите температуру в градусах Цельсия: ").replace(',', '.'))
    
    # Вычисление температуры в разных шкалах с округлением
    kelvin = f"{celsius + 273.15:.2f}"
    fahrenheit = f"{(celsius * 9/5) + 32:.2f}"
    reaumur = f"{celsius * 4/5:.2f}"
    
    # Вывод результатов с использованием одного print()
    print(f"Температура {celsius}°C в разных шкалах:\nКельвин: {kelvin} K\nФаренгейт: {fahrenheit}°F\nРеомюр: {reaumur}°Ré")

# Обработка неверного выбора
else:
    print("Неверный выбор. Пожалуйста, выберите 1 или 2.")
