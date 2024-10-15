def decimal_to_binary(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_to_binary(n // 2) + str(n % 2)

def decimal_to_octal(n):
    if n == 0:
        return "0"
    elif n < 8:
        return str(n)
    else:
        return decimal_to_octal(n // 8) + str(n % 8)

# Ввод числа с клавиатуры
number = int(input("Введите десятичное число: "))

# Перевод в двоичную и восьмеричную системы
binary_result = decimal_to_binary(number)
octal_result = decimal_to_octal(number)

# Вывод результатов
print(f"Двоичное представление: {binary_result}")
print(f"Восьмеричное представление: {octal_result}")

