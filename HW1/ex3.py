inf = float('Inf')
inf_ = float('-Inf')
quarters = {1: [(0, inf), (0, inf)], 2: [(0, inf_), (0, inf)], }

print("Введите координаты: ")
x = int(input("X: "))
y = int(input("Y: "))
if (x > 0) and (y > 0):
    print("1")
elif (x < 0) and (y > 0):
    print("2")
elif (x < 0) and (y < 0):
    print("3")
else:
    print("4")