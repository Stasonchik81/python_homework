import random as rd

user_1 = {
    "id": 1,
    "name": '',
    "take": 0
}
user_2 = {
    "id": 2,
    "name": '',
    "take": 0
}

game = {"bank": 2021,
"max_get": 28,
"move": user_1}

# Функция броска кубика
def get_lot():
    score = rd.randint(1, 6)
    return score

# Жребий
def get_move(user):
    print(f"{user['name']} бросает кубик!")
    user['take'] = get_lot()
    print(f"Выпало {user['take']}")

# Делаем ход
# def move():
    
    

# Представимся
user_1['name'] = input("Введите имя первого игрока: ")
user_2['name'] = input("Введите имя второго игрока: ")

while user_1['take'] == user_2['take']:
    get_move(user_1)
    get_move(user_2)
game["move"] = user_1 if user_1['take'] > user_2['take'] else user_2
    
while game["bank"] > 0:
    print(f"Ходит {game['move']['name']}")
    temp_ = int(input(f"Введите количество конфет: "))
    while temp_ not in range(1, 29):
        print("Неправильное количество!")
        temp_ = int(input(f"Введите количество конфет: "))
    if game["bank"] < temp_:
        print("Конфет не хватает!")
    elif game["bank"] == temp_:
        print(f"Победил {game['move']['name']}")
        break
    else: 
        game["bank"] -= temp_
    game["move"] = user_2 if game["move"] == user_1 else user_1


