# prime factors of a number

import math

num = int(input("Введите число: "))

def prime_factors(n: int):
    result = [1]
    for i in range(2, n):
        while (n%i == 0) and (n > 1):
            result.append(i)
            n = n / i
    return result

print(prime_factors(num))