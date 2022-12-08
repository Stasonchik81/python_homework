# Удаляем слова

my_str = 'Я люблю Джавуабв иабв Питон'

x = list(filter(lambda s: 'абв' not in s ,my_str.split()))
print(" ".join(x))

exit()
# найти все пропущенные числа в последовательности
with open("test.txt", 'r') as data:
    my_list = list(map(int, data.read().split()))
    print(my_list)

# список пропущенных значений
find_ = []
for i in range(1, len(my_list)):
    if my_list[i] - 1 != my_list[i - 1]:
        d = my_list[i] - my_list[i - 1]
        for j in range(d-1):
            temp = my_list[i - 1] + j
            find_.append(temp + 1)

print(find_)