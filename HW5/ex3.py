char_ = "."
phase = 'X'
win_lines = []

def togglePhase():
    global phase
    if phase == 'X': 
        phase = 'O'
    else: phase = 'X'

def render_fields(fields):
    for i in fields:
        for j in i:
            print(j, end='   ')
        print('\n')

def init_fields(size: int, char_: str):
    rows_ = []
    for i in range(1, size+1):
        cols_ = []
        for j in range(1, size+1):
            cols_.append(char_)
        rows_.append(cols_)
    return rows_

def input_point(name: str):
    point = tuple(int(i) for i in input(f"{name} введите координаты точки через пробел (ряд столбец): ").split())
    return point
    

def step(game: list, point: tuple, char_: str):
    if game[point[0]-1][point[1]-1] == '.':
        game[point[0]-1][point[1]-1] = char_
        return True
    else:
        print('поле уже занято!')
        return False

def input_name():
    return input("Введите имя игрока:")

def get_win_lines(matrix): #генератор проверки линий
    global win_lines
    len_ = len(matrix)
    horizontals = [''.join(i) for i in matrix]
    temp = []
    for i in range(len_):
        x = []
        for j in range(len_):
            x.append(matrix[j][i])
        temp.append(x)
    verticals = [''.join(i) for i in temp]
    temp = []
    crosses = []
    for i in range(len_):
        temp.append(matrix[i][i])
    crosses.append(''.join(temp))
    temp = []
    for i in range(len_):
        temp.append(matrix[len_-1-i][i])
    crosses.append(''.join(temp))
    win_lines = horizontals + verticals + crosses


def isWin(win_lines):
    str_x = 'X' * 3
    str_o = 'O' * 3
    return str_x in win_lines or str_o in win_lines

user_1 = input_name()
user_2 = input_name()
map = init_fields(3, char_)
render_fields(map)

while(not isWin(win_lines)):
    if(step(map, input_point(name = user_1 if phase == 'X' else user_2), phase)):
        render_fields(map)
        get_win_lines(map)
        if isWin(win_lines):
            print(f"Победил {user_1 if phase == 'X' else user_2}")
            break
        togglePhase()


