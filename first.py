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

def move(x, y, map, side):
    map[y][x] = "_"
    if side == "left":
        x -= 1
        if x < 0:
            x = len(map) - 1

    elif side == "right":
        x += 1
        if x > len(map) - 1:
            x = 0

    elif side == "up":
        y -= 1
        if y < 0:
            y = len(map) - 1

    elif side == "down":
        y += 1
        if y > len(map) - 1:
            y = 0

    map[y][x] = "x"
    return x, y, map


def main():
    size = hello()
    map = pole(size)
    x, y = 0, 0
    map[y][x] = "x"
    while True:
        show(map)
        side = input("left, up, right, down")
        x, y, map = move(x, y, map, side)

main()