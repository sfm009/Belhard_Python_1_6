"""
Написать рекурсивную функцию fibonacci, которая будет возвращать n-ый элемент
"""


def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(3))
