"""
Написать генератор factorial, который возвращает подряд значения факториала

Например:

factorial_gen = factorial()

next(factorial_gen) -> 1
next(factorial_gen) -> 2
next(factorial_gen) -> 6
next(factorial_gen) -> 24
"""
from math import factorial


def factorial_gen(n: int):
    for i in range(1, n + 1, 1):
        yield factorial(i)


for item in factorial_gen(5):
    print(item)

