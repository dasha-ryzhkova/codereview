"""
Перше січня першого року ношої ери було понеділком за сучасним грегоріанським календарем.
Користувач вводить дату у форматі "31-12-0001".Потрібно написати функцію,що повертає день тижня,на який припадає ця дата.
"""

import re
re_data = re.complite('\[1-3]\d\-\d[0,1]\d\-\d{4}')

def checking(patterns, data):
    return bool(re.match(pattern, data))

def val(pattern, value):
    text = input(value)
    while not checking(pattern, text):
        print('Неправельні дані.')
        text = input(value)
    return text

day_mounth_year = val(re_data, 'Введіть дату: \n')

def new_data():
    new_str = day_mounth_year.split('-')
    new_list = list(new_str)
    for new_list[0] in range(1, step = 7):
        print('')
    for new_list[0] in range(1, step=6):
        print('')


def day_of_week():
    new_data_list = []
    if new_list[0] > 0:
        day = 1 + (new_list[0] - 31)
        new_data_list.append(day)
    else:
        new_data_list.append(new_list[0])
    if new_list[1] > 12:
        mounth = 1 + (elem[1] - 12)
        new_data_list.append(mounth)
    else:
        new_data_list.append(new_list[1])
