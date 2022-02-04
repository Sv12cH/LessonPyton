#Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма. Например, прибыль — выручка больше издержек,
# или убыток — издержки больше выручки. Выведите соответствующее сообщение.

TR=float(input("Введите выручку фирмы за интересующий Вас период:"))
TC=float(input("Введите издержки фирмы за данный период:"))

V=float(TR-TC)
if V>0:
    print("Прибыль Вашей фирмы за текущий период составила:", V, "рублей")

# Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

    R = V / TC*100
    print("Рентабельность деятельности за данный период:",R, "%")

    P=int(input("Введите численность сотрудников Вашей фирмы:"))
    Lr=R/P
    print("Производительность труда в Вашей фирме, в данный период:", Lr, "руб./чел.")

elif V<0:
    print("Убыток Вашей фирмы за текущий период:", V, "рублей")

else:
        print("Вы участвовали в финансовых потоках, но наработали:", V, "рублей")