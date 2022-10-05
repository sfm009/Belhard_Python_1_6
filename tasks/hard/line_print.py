"""
Написать рекурсивную функцию  line_print, которая принимает 1 аргумент - список

Функция печатает каждых элемент на новой строке.

Если элемент списка - список, то его элементы должны выводиться с отступом
относительно родительского на 4 пробела

Например:

some_list = [1, 2, [1, 2, [5, 7], 3], 8]

line_print(some_list)
1
2
    1
    2
        5
        7
    3
8
"""


some_list = [1, 2, [1, 2, [5, 7], 3], 8]


def line_print(array, counter=0):
    for item in array:
        if isinstance(item, list):
            counter += 1
            line_print(item, counter)
            counter -= 1
        else:
            print(4 * counter * " ", item)


line_print(some_list)
