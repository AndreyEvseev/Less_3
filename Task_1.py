from Func_list import fill_list_int as func

def sum_elements_odd_position(user_list) -> int:
    sum_odd = 0
    for i in range(1, len(user_list)):
        if i % 2 != 0:
            sum_odd = sum_odd + user_list[i]
    return sum_odd

n = int(input('Количество элементов списка: '))
b1 = int(input('Граница 1 диапазона значений элементов списка: '))
b2 = int(input('Граница 2 диапазона значений элементов списка: '))
source_list = func(n, b1, b2)
sum_odd = sum_elements_odd_position(source_list)
print(f'Сумма элементов списка {source_list}, стоящих на нечётной позиции = {sum_odd};')
