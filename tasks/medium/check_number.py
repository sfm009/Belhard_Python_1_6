"""
Написать рекурсивную функцию check_number, которая должна возвращать True,
если переданное ей число n является степенью двойки (1 тоже степень двойки) и
False, если нет

Нельзя пользоваться операцией возведения в степень
"""


def check_number(n):
    if n == 1:
        result = True
    else:
        while n > 1:
            if n % 2 != 0:
                result = False
                break
            else:
                n /= 2
            result = True
    return result


print(check_number(5))
