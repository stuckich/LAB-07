from functions import select_numbers

test_list_1 = [-5, 0, 2, 5]
threshold_1 = 2
result_1 = select_numbers(test_list_1, threshold_1)

print("--- Тест 1 (Контрольный список из условия) ---")
print(f"Исходный список: {test_list_1}")
print(f"Порог: {threshold_1}")
print(f"Результат (пустой выбор): {result_1}\n")  # Ожидается []


test_list_2 = [12, 4, 7, 8, 2, 10, 8, -4, 14]
threshold_2 = 5
result_2 = select_numbers(test_list_2, threshold_2)

print("--- Тест 2 (Пример с совпадениями и повторами) ---")
print(f"Исходный список: {test_list_2}")
print(f"Порог: {threshold_2}")
print(f"Результат: {result_2}\n")  # Ожидается [12, 8, 10, 8, 14]


print("--- Интерактивный тест ---")
try:
    user_input = input("Введите целые числа через пробел: ")
    user_list = [int(x) for x in user_input.split()]
    
    user_threshold = float(input("Введите неотрицательный порог (threshold): "))
    if user_threshold < 0:
        print("Предупреждение: порог должен быть неотрицательным. Сброс в 0.")
        user_threshold = 0
        
    user_result = select_numbers(user_list, user_threshold)
    print(f"Результат фильтрации: {user_result}")

except ValueError:
    print("Ошибка ввода! Убедитесь, что вводите только числа.")
