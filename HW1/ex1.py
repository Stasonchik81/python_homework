num_days = list(range(1, 8))
# print (days)
num_day = int(input("Введите номер дня недели: "))
if num_day in num_days:
    print("нет") if num_day < 6 else print("да")
else:
    print("неверный номер дня")
