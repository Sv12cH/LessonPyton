# Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

with open('test_51.txt', 'r', encoding="utf-8") as file:
    my_list = file.readlines()
    for i in range(len(my_list)):
        new_l = my_list[i].split()
        print(f'Количество строк в файле "test_51" -  {len(my_list)}. В {i + 1} строках(е) {len(new_l)} слов(а)')