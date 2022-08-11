"""
Написать функцию triangular_sequence, которая принимает n и возвращает
последовательность следующего вида:

1
22
333
4444
55555
...

Например:

n = 3:
1
22
333

n = 6:
1
22
333
4444
55555
666666
"""


def triangular_sequence(n: int):
    print(str(n) * n)
    n -= 1
    if n >= 0:
        triangular_sequence(n)

triangular_sequence(6)