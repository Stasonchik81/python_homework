# random list
import random


def rand_list(len_, min_: int, max_: int, type_: str = 'int', dig: int = 2):
    list_ = []
    if type_ == 'int':
        for i in range(len_):
            list_.append(random.randint(min_, max_))
    elif type_ == 'float':
        for i in range(len_):
            list_.append(round(random.uniform(min_, max_), dig))
    else:
        print("error of type")
    return list_


def main():
    print(rand_list(5, 1, 10, 'float', 1))


if __name__ == "__main__":
    main()