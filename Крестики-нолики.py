from random import randint


def hay_player():
    print("""Добро пожаловать!
Сыграем в крестики - нолики!
Формат заполнения x/y""")


def check_random():
    while True:
        rand = input("Хотите играть против рандома (Да\Нет)? ")
        if rand == "Да":
            return True
        elif rand == "Нет":
            return False
        else:
            print("Формат ответа Да или Нет!")
            continue


def playground():
    print("")
    print("   0   1   2")
    for i in range(3):
        print(f"{i} {play[i][0]} {play[i][1]} {play[i][2]}")


def player_X():
    while True:
        step = list(map(int, input("X ваш ход : ").split()))
        a, b = step[0], step[1]
        if len(step) != 2:
            print("Нужны координаты x и y!")
            continue
        elif a > 2 or b > 2:
            print("Выход за пределы!")
            continue
        elif play[a][b] != "| |":
            print("Клетка занята!")
            continue
        else:
            play[a][b] = "|X|"
            break


def player_O():
    while True:
        step = list(map(int, input("O ваш ход : ").split()))
        a, b = step[0], step[1]
        if len(step) != 2:
            print("Нужны координаты x и y!")
            continue
        elif a > 2 or b > 2:
            print("Выход за пределы!")
            continue
        elif play[a][b] != "| |":
            print("Клетка занята!")
            continue
        else:
            play[a][b] = "|O|"
            break


def player_vs_ran():                         # Решил добавить якобы игру с компьютером
    while True:
        a, b = randint(0, 2), randint(0, 2)  # Но решил что не буду париться и пускай ставит рандомно
        if play[a][b] != "| |":
            continue
        else:
            play[a][b] = "|O|"
            break


def winner():
    win = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
           ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
           ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for i in win:
        choose = []
        for c in i:
            choose.append(play[c[0]][c[1]])
        if choose == ["|X|", "|X|", "|X|"]:
            print("Победитель X!")
            return True
        if choose == ["|O|", "|O|", "|O|"]:
            print("Победитель O!")
            return True
    return False


play = [["| |"] * 3 for i in range(3)]
hay_player()
playground()
count = 0
if check_random():
    while True:
        count += 1
        player_X()
        playground()
        if winner():
            break
        if count == 9:
            print("Ничья!")  # Поставил проверку здесь ибо если с Х начинается
            break            # то Х и будет последним
        player_vs_ran()
        playground()
        if winner():
            break
else:
    while True:
        count += 1
        player_X()
        playground()
        if winner():
            break
        if count == 9:
            print("Ничья!")
            break
        player_O()
        playground()
        if winner():
            break
