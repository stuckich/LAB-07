from functions import sum_digits, average, normalize_text


def main():
    try:
        user_num = int(input("Введите целое число для подсчета суммы цифр: "))
        print(f"Сумма цифр модуля: {sum_digits(user_num)}")
    except ValueError:
        print("Ошибка: введено не целое число.")

    print("-" * 30)

    print("Введите числа для расчета среднего значения (через пробел).")
    print("Для создания пустого списка просто нажмите Enter:")
    raw_numbers = input("> ").split()
    
    numbers_list = []
    for x in raw_numbers:
        try:
            numbers_list.append(float(x))
        except ValueError:
            pass

    avg_result = average(numbers_list)
    if avg_result is None:
        print("Среднее значение: Нет данных")
    else:
        print(f"Среднее значение: {avg_result}")

    print("-" * 30)

    user_text = input("Введите произвольный текст с лишними пробелами:\n")
    normalized = normalize_text(user_text)
    print(f"Нормализованный текст:\n'{normalized}'")


if __name__ == "__main__":
    main()
