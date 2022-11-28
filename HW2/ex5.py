# shuffle list
import random

number = int(input("Введите число: "))

my_list = list(range(1, number))
print(my_list)

# Встроенная функция в модуль random
# random.shuffle(my_list)
# print(my_list)

# Моя реализация функции:
def My_shuffle(my_list):   
    for i in range(0, len(my_list) - 1):
        idx = random.randint(0, len(my_list) - 1)
        temp = my_list[i]
        my_list[i] = my_list[idx]
        my_list[idx] = temp

My_shuffle(my_list)
print(my_list)
