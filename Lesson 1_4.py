# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input("Введите целое число (не жадничайте, давайте число подлиннее):"))

number_max = 0

while number > 0:
    number_check = number % 10
    if number_check > number_max:
        number_max = number_check
    number = number // 10

print(f" Максимальная цифра в Вашем числе, это {number_max}")
