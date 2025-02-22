import move
from random import randint

def hello():
    return int(input("Введите размер поля: "))

def pole(a):
    map = []
    for _ in range(a):
        row = []
        for _ in range(a):
            if randint(1, 3) == 1:
                row.append('#')
            else:
                row.append('_')
        map.append(row)
    return map

def show(map):
    for row in map:
        print(" ".join(row))

def main():
    size = hello()
    map = pole(size)
    x, y = 0, 0
    map[y][x] = "x"

    while True:
        show(map)
        side = input("left, up, right, down")
        x, y, map = move.game(x, y, map, side)


main()