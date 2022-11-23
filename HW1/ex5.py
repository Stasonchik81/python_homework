import math

print("Ввод координат точек (через пробел)")
coordinates = []

for i in range(1, 3):
    input_string = input(f'Введите координаты точки {i}: ').split()
    point = tuple(map(int, input_string))
    coordinates.append(point)

def Get_distance(points):
    s = math.sqrt((points[0][0] - points[1][0])**2 + (points[0][1] - points[1][1])**2)
    distace = round(s, 2)
    return distace

d = Get_distance(coordinates)
print(f'Расстояние между точками {coordinates[0]} - {coordinates[1]} = {d}')
