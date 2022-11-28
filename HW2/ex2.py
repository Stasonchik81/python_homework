#  n - factorial

number = int(input("Введите число: "))

def factorial (num):
    if num == 1: 
        return num
    else: 
        return num * factorial(num - 1)

f = factorial(number)
print(f"Факториал числа {number} -> {f}")   