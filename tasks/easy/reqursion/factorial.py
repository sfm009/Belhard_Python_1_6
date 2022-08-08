"""
Написать рекурсивную функцию factorial, которая будет возвращать n-ый элемент

5! = 1 * 2 * 3 * 4 * 5 = 125
"""


def factorial(n=5):
    if n == 0:
        return 1
    return factorial(n - 1) * n


print(factorial())

