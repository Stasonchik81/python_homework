# list of non-repeating elements

from My_modules import my_lib

my_list = my_lib.rand_list(9, 1, 15)

def non_repeating(list_):
    non_repeat_list = [i for i in list_ if list_.count(i) < 2]
    return non_repeat_list

print(my_list)

print(non_repeating(my_list))