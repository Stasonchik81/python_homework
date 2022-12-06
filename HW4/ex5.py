# summ of pare elements in polynomials
from ex4 import set_polinome_list as set_list 

with (open("polinome1.txt", "r")) as data_1:
    first_p_list = data_1.read().split(" + ")
    last_item_1 = (first_p_list.pop().split(" ")).pop(0)

with (open("polinome2.txt", "r")) as data_2:
    second_p_list = data_2.read().split(" + ")
    last_item_2 = (second_p_list.pop().split(" ")).pop(0)

# степень многочлена
k = len(first_p_list)

# списки коэффициентов многочленов
items_1 = list(map(int, [i[:i.find('*')] for i in first_p_list])) + [int(last_item_1)]
items_2 = list(map(int, [i[:i.find('*')] for i in second_p_list])) + [int(last_item_2)]
items_3 = list(map(sum, zip(items_1, items_2)))

final_p_list = set_list(items_3, k)
print(final_p_list)

with (open(f"polinome3.txt", 'w')) as polinome:

    print(" + ".join(final_p_list), file=polinome, end="")
    polinome.write(" = 0")