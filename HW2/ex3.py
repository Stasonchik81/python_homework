#  sum of list numbers

number = int(input("Введите длинну последовательности: "))

def rule(n):
    return round((1 + 1/n)**n, 2)

def Get_list_nums(length, func):
    result = []
    for n in range(1, length+1):
        x = func(n)
        result.append(x)
    return result


def Summ(list_nums):
    result = 0
    for n in list_nums:
        result += n
    return result

my_list = Get_list_nums(number, rule)
print(f"Для n = {number} Сумма = {Summ(my_list)}")