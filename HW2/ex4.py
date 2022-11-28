# multiple elemets in list on indexes

number = int(input("Введите число: "))

list_of_elements = []
for i in range(-number, number+1):
    list_of_elements.append(i)
print(f"Элементы - {list_of_elements}")

list_of_indexes = []
str_index = input("Введите индексы через пробел: ")
for i in str_index.split():
    list_of_indexes.append(int(i))

result = list_of_elements[list_of_indexes[0]]
for i in range(1, len(list_of_indexes)):
    result *= list_of_elements[list_of_indexes[i]]

print(f"Вывод = {result}")