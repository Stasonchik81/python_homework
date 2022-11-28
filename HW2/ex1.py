# summ of digits

str_digit = input("Введите число")


def Sum_of_digits(num):
    sum = 0
    for d in num:
        sum += int(d)
    return sum


data = str_digit.split(",")
result = 0
for i in data:
    result += Sum_of_digits(i)
print(f' sum of digit in {str_digit} = {result}')
