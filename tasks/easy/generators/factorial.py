"""
Написать генератор factorial, который возвращает подряд значения факториала

Например:

factorial_gen = factorial()

next(factorial_gen) -> 1
next(factorial_gen) -> 2
next(factorial_gen) -> 6
next(factorial_gen) -> 24
"""
import math


def factorial(n=5):
    for i in range(1, n + 1, 1):
        yield math.factorial(i)


for item in factorial():
    print(item)
