# difference between min and max fractional parts

from My_modules import my_lib

my_list = my_lib.rand_list(5, 1, 10, "float", 2)


def min_in_fract_part(list_: [float], digits):
    min_ = list_[0] % 1
    for i in list_:
        f = round(i % 1, digits)
        if f < min_:
            min_ = f
    return min_


def max_in_fract_part(list_: [float], digits):
    max_ = list_[0] % 1
    for i in list_:
        f = round(i % 1, digits)
        if f > max_:
            max_ = f
    return max_


def diff_min_max_fractional_parts(list_: [float], digits):
    return round(max_in_fract_part(list_, digits) - min_in_fract_part(list_, digits), digits)


print(f"{my_list} => {diff_min_max_fractional_parts(my_list, 2)}")
