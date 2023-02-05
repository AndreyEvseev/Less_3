import random
from Func_list import fill_list_float as func

def float_to_int(user_list): # замена вещественного числа на целое для проверки функции "def integer_exclusion"
    pos = random.randint(0, len(user_list)-1)
    user_list[pos] = int(user_list[pos])
    return user_list

def integer_exclusion(user_list): # исключение целых чисел из первоначального списка
    transform_list = [user_list[i] for i in range(len(user_list)) if user_list[i] % 1 != 0]
    print(transform_list)
    return transform_list

def difference_fractional_parts(user_list):
    processed_list = integer_exclusion(user_list)
    min_element = max_element = processed_list[0] % 1
    for i in range(1, len(processed_list)):
        if processed_list[i] % 1 < min_element:
            min_element = processed_list[i] % 1
        elif processed_list[i] % 1 > max_element:
            max_element = processed_list[i] % 1
        else:
            continue
    diff = round(max_element - min_element, 5)
    return diff

n = int(input('Количество элементов списка: '))
b1 = int(input('Граница 1 диапазона значений элементов списка: '))
b2 = int(input('Граница 2 диапазона значений элементов списка: '))
source_list = func(n, b1, b2) # формирование списка случайных вещественных чисел
source_list = float_to_int(source_list) # замена одного элемента на целое для проверки функции "def integer_exclusion"
diff = difference_fractional_parts(source_list)
print(f'{source_list} => {diff};')
