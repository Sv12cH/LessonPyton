# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.


number = int(input("Введите, пожалуйста, целое, положительное число:"))

number_2 = int(f'{number}{number}')

number_3 = int(f'{number}{number}{number}')

resalt = int(number + number_2 + number_3)
print(resalt)
