# generate polynomial

import random as rd

k = int(input("Введите степень многочлена: "))
cof = tuple([rd.randint(1, 100) for i in range(k + 1)])
list_of_polinom = []

for i in range(k + 1):
    if k - i == 1:
        list_of_polinom.append(f"{cof[i]}*X")
    elif i == k:
        list_of_polinom.append(f"{cof[i]}")
    else:
        list_of_polinom.append(f"{cof[i]}*(X**{k-i})")

with (open("polinome.txt", 'w')) as poli:

    print(" + ".join(list_of_polinom), file=poli, end="")
    poli.write(" = 0")