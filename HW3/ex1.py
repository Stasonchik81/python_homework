# summ of odd elements in my list

from My_modules import my_lib

my_list = my_lib.rand_list(5, 1, 10)

def sum_of_odd(list_: [int]):
    result = 0
    elements = []
    for i in range(1, len(list_) - 1, 2):
        result += list_[i]
        elements.append(list_[i])
    return (result, elements)

my_result = sum_of_odd(my_list)
print(f"{my_list} -> на нечётных позициях элементы {my_result[1]}, ответ {my_result[0]}")
