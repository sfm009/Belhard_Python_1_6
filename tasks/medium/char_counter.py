"""
Написать функцию count_char, которая принимает строковое значение STR_VAL,
из которого создает и возвращает словарь, следующего вида:
{
    'буква': количество-вхождений-в-строку
}

например: {
    'p': 2,
    'y': 1,
    ...
}

Нельзя пользоваться collections.Counter!
"""
STR_VAL = 'python is the fastest-growing major programming language'


def count_char(STR_VAL: str):
    count_char_dict = {}
    str_new = "".join(set(STR_VAL))
    for i in range(len(str_new)):
        key = str_new[i]
        value = STR_VAL.count(str_new[i])
        count_char_dict[key] = value
    return count_char_dict

print(count_char(STR_VAL))