import math
from Func_list import fill_list_int as func

def product_pairs(user_list) -> list:
    new_list = []
    for i in range(0, math.ceil(len(user_list)/2)):
        new_list.append(user_list[i]*user_list[len(user_list)-1-i])
    return new_list

n = int(input('Количество элементов списка: '))
b1 = int(input('Граница 1 диапазона значений элементов списка: '))
b2 = int(input('Граница 2 диапазона значений элементов списка: '))
source_list = func(n, b1, b2)
result_list = product_pairs(source_list)
print(f'{source_list} => {result_list};')