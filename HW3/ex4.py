# decimal to binare

num = int(input("Введите число: "))

def decimal_to_binar(num: int):
    result = 0
    i = 0 
    while num > 0:
        result += (num % 2)*pow(10, i)
        num /= 2
        num = int(num)
        i += 1
    return result

print(f"{num} => {decimal_to_binar(num)}")
