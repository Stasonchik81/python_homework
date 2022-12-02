# multiple pare of elements

from My_modules import my_lib

my_list = my_lib.rand_list(7, 1, 10)

def multi_pare_of_elements(list_):
    result = []
    len_ = len(list_)
    for i in range(len_):
        if i >= len_/2:
            return result
        multi_ = list_[i]*list_[len_-1-i]
        result.append(multi_)


print(f"{my_list} => {multi_pare_of_elements(my_list)}")