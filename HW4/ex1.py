# calculation with set accuracy

from math import pi as PI

print(PI)

def my_round_float(num: float, d: float = 1):
    temp = (num/d)*10
    if temp%10 >= 5:
        return (int(temp/10)+1)*d
    else:
        return int(temp/10)*d

result = my_round_float(PI, 0.001)
print(result)

