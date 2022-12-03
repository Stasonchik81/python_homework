# list with nego fibonachi
num = int(input("Введите число: "))

def fibonacchi(k: int):
    if (k == 1) or (k == 2):
        return 1
    else:
        return fibonacchi(k-1) + fibonacchi(k-2)

def nego_fibonacchi(k: int):
    if k == 1:
        return 1
    elif k == 0:
        return 0
    else:
        return nego_fibonacchi(k + 2) - nego_fibonacchi(k + 1)


def list_fibonacchi(k: int):
    result = [0]
    for i in range(1, k+1):
        result.append(fibonacchi(i))
    result.reverse()
    for j in range(1, k+1):
        result.append(nego_fibonacchi(-j))
    result.reverse()
    return result

print(f"Для к = {num} ряд - {list_fibonacchi(num)}")