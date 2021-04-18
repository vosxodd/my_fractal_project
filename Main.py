from turtle import *
colors = ['red', 'blue', 'green', 'purple', 'pink', 'orange', 'red']

def star(order, size):
    pensize(5)
    if order == 0:
        for i in colors:
            color(i)
            fd(size)
    else:
        count = 0
        angle = 144
        while count <= 5:
            star(order - 1, size)
            right(angle)
            count += 1


def main():
    speed(50000000)
    up()
    goto(0,0)
    down()
    n = int(input('Глубина рекурсии (рекомендовано 3): '))
    a = int(input('Длина стороны (рекомендовано 15: '))
    star(n, a)
    hideturtle()
    mainloop()
main()
