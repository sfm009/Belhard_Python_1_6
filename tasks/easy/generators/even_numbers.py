"""
Написать генератор get_even_number, который возвращает подряд четные числа

Например:

even_gen = get_even_number()

next(even_gen) -> 2
next(even_gen) -> 4
next(even_gen) -> 6
"""


def get_even_number(n=10):
    for i in range(0, n - 1, 2):
        yield i + 2

for item in get_even_number():
    print(item)

