def main():
    student_name = input("Введите имя студента: ").strip()

    if not student_name:
        print("Введено пустое имя. Пожалуйста, введите имя студента.")
        return

    grade_input = input("Введите оценку студента: ").strip()

    if not grade_input.isdigit():
        print("Введено некорректное значение. Пожалуйста, введите число.")
        return

    grade = int(grade_input)
    
    if grade < 1 or grade > 12:
        print("Введена некорректная оценка. Пожалуйста, введите число от 1 до 12.")
        return

    level = ""
    if grade in [1, 2, 3]:
        level = "Начальный"
    elif grade in [4, 5, 6]:
        level = "Средний"
    elif grade in [7, 8, 9]:
        level = "Достаточный"
    elif grade in [10, 11, 12]:
        level = "Высокий"

    print(f"Имя студента: {student_name}. Уровень: {level}")

if __name__ == "__main__":
    main()
