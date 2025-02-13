def pole(a):
    map = []
    for i in range(a):
        map.append(['_'] * a)
    return map

def show(map):
    for row in map:
        print(" ".join(row))
