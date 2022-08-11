"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""

some_list = [1, 2, 3, 2, 5, 6, 1, 7]


def yes_or_no(some_list):
    for i in range(len(some_list)):
        element = some_list[i]
        new_list = list(some_list[0 : i + 1])
        counter = new_list.count(element)
        if counter != 1:
            print('Yes')
        else:
            print('No')


yes_or_no(some_list)