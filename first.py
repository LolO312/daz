import game
from random import randint

def hello():
    return int(input("Введите размер поля: "))

def pole(a):
    map = []
    for i in range(a):
        map.append(['_'] * a)
    return map

def show(map):
    for row in map:
        print(" ".join(row))


def main():
    size = hello()
    map = pole(size)
    x, y = 0, 0
    map[y][x] = "x"
    a, b = randint(1, size), randint(1, size)
    map[b][a] = "0"

    while True:
        show(map)
        side = input("left, up, right, down")
        x, y, map = game.move(x, y, map, side)

main()