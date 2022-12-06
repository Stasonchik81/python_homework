# generate polynomial

import random as rd

k = int(input("Введите степень многочлена: "))
cof = tuple([rd.randint(1, 100) for i in range(k + 1)])

def set_polinome_list(indexes: list[int], k: int = 6):
    result_p_list = []
    for i in range(k + 1):
        if k - i == 1:
            result_p_list.append(f"{indexes[i]}*X")
        elif i == k:
            result_p_list.append(f"{indexes[i]}")
        else:
            result_p_list.append(f"{indexes[i]}*(X**{k-i})")
    return result_p_list

def main():
    list_of_polinom_1 = set_polinome_list(cof, k)

    with (open(f"polinome1.txt", 'w')) as poli:

        print(" + ".join(list_of_polinom_1), file=poli, end="")
        poli.write(" = 0")


if __name__ == "__main__":
    main()

