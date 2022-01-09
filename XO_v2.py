def great():
    print("----------------------")
    print("   Приветствуем вас   ")
    print("        в игре        ")
    print("    крестики-нолики   ")
    print("----------------------")
    print("  формат ввода: x y   ")
    print("  x - номер строки    ")
    print("  y - номер столбца   ")

def show():
    print()
    print("   | 0 | 1 | 2 | ")
    print(" --------------- ")
    for i, row in enumerate(field):
        row_str = f" {i} | {' | '.join(row)} | "
        print(row_str)
        print(" --------------- ")
    print()

def out_green(text):
    print("\033[32m {}".format(text))

def ask(f,user):
    while True:
        cords = input(f"    Ваш ход '{user}' через пробел:  ").split()
        if len(cords) != 2:
            print(" Введите 2 координаты ")
            continue
        x, y = cords
        if not (x.isdigit()) or not (y.isdigit()):
            print(" Ввелите число ")
            continue
        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона ")
            continue
        if field[x][y] != " ":
            print(" Клетка занята ")
            continue
        return x, y

def check_win(f,user):
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(f[c[0]][c[1]])
        if symbols == [user, user, user]:
            return True
    return False

great()
field = [[" "] * 3 for i in range(3)]
num = 0
while True:
    num += 1
    out_green(show)
    show()
    if num % 2 == 1:
        user = "x"
    else:
        user = "o"
    x, y = ask(field,user)
    field[x][y] = user
    if check_win(field,user):
        show()
        print(f"Выиграл '{user}' !")
        break
    if num == 9:
        show()
        print(" Ничья ")
        break