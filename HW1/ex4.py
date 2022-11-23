
table_of_ranges = {1: 'x>0 and y>0', 2: 'x<0 and y>0',
                   3: 'x<0 and y<0', 4: 'x>0 and y<0'}


def Get_range(quarter):
    if quarter in range(1, 5):
        return table_of_ranges[quarter]
    else:
        print("Ошибка ввода данных!")
        return False


q = int(input("Введите номер четверти (1-4): "))
range_ = Get_range(q)
if range_:
    print(range_)
