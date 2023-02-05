import random

# Функция для формирования списка случайных вещественных чисел
def fill_list_float(n, border1, border2): 
    if border1 < border2:
        min_bord, max_bord = border1, border2
    else:
        min_bord, max_bord = border2, border1
    new_list = [round(random.randint(min_bord, max_bord) + random.random(), 5)]
    for i in range(1, n):
        new_list.append(round(random.randint(min_bord, max_bord) + random.random(), 5))
        i += 1
    return new_list

# Функция для формирования списка случайных целых чисел
def fill_list_int(n, border1, border2): 
    if border1 < border2:
        min_bord, max_bord = border1, border2
    else:
        min_bord, max_bord = border2, border1
    new_list = [random.randint(min_bord, max_bord)]
    for i in range(1, n):
        new_list.append(random.randint(min_bord, max_bord))
        i += 1
    return new_list
