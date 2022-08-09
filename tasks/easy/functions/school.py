"""
Написать композицию из функций (не чистых функций)

Имеется словарь SCHOOL_DATA с данными школы класс-количество учеников

- Функция incr_students, которая принимает SCHOOL_DATA, название класса и
    увеличивает количество учеников на 1
- Функция decr_students, которая принимает SCHOOL_DATA, название класса и
    уменьшает количество учеников на 1, но не меньше 0
- Функция add_class, которая принимает SCHOOL_DATA, название класса и добавляет
    класс в словарь с количеством учеников 0
- Функция remove_class, которая принимает SCHOOL_DATA, название класса и удаляет
    класс из словаря
- Функция calc_students, которая принимает SCHOOL_DATA и возвращает кол-во
    учеников во всей школе
"""
school_data = {
    '1a': 15,
    '1b': 23,
    '2a': 13,
    '2b': 30
}


def incr_students(school_data: dict, cls):
    school_data[cls] += 1


def decr_students(school_data: dict, cls):
    school_data[cls] -= 1


def add_class(school_data: dict, cls):
    school_data[cls] = 0


def remove_class(school_data: dict, cls):
    school_data.pop(cls)


def calc_students(school_data: dict):
    result = sum(school_data.values())
    return result



incr_students(school_data, cls='1a')
decr_students(school_data, cls='1b')
add_class(school_data, cls='3a')
remove_class(school_data, cls='2a')
print(calc_students(school_data))
