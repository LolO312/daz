def game(x, y, map, side):
    x_old, y_old = x, y
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

    if map[y][x] == '#':
        print("Вы не можете этого сделать")
        return x_old, y_old, map
    map[x_old][y_old] = "_"
    map[y][x] = "x"

    return x, y, map