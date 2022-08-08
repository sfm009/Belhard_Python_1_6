"""
Написать генератор get_even_number, который возвращает подряд четные числа

Например:

even_gen = get_even_number()

next(even_gen) -> 2
next(even_gen) -> 4
next(even_gen) -> 6
"""


def get_eve_number(n):
    for i in range(0, n, 2):
        yield i + 2

for item in get_eve_number(6):
    print(item)


even_gen = get_eve_number(20)
