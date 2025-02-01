def hello():
    return int(input("Введите размер поля: "))

def pole(a):
    for i in range(a):
        print(a * " _ ")

def mainn():
    side = hello()
    pole(side)

mainn()