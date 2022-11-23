print("Введите координаты: ")
x = int(input("X: "))
y = int(input("Y: "))
if (x != 0) and (y != 0):
    if (x > 0) and (y > 0):
        print("1 четверть")
    elif (x < 0) and (y > 0):
        print("2 четверть")
    elif (x < 0) and (y < 0):
        print("3 четверть")
    else:
        print("4 четверть")
else:
    print("координаты не должны быть равны 0!")
