# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.


with open("text_3.txt", 'r', encoding='utf-8') as list_empl:
    f_average_salary = 0
    all_list_empl = list_empl.readlines()
    for line in all_list_empl:
        s_name, salary = line.split()
        salary = float(salary)
        f_average_salary += salary
        if salary < 20000:
            print(f"\t{s_name} {salary}")
    if len(all_list_empl) > 0:
        f_average_salary /= len(all_list_empl)
        print(f"\tСредняя зарплата: {f_average_salary:.2f}\n")

