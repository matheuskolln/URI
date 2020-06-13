from math import sqrt
while True:
    try:
        xf, yf, xo, yo, vo, ru, rc = map(int, input().split(' '))

        dfo = sqrt((xf - xo) ** 2 + (yf  - yo) ** 2)
        dfo += vo * 1.5
        ra = ru + rc

        if dfo > ra:
            print('N')
        else:
            print('Y')

    except EOFError:
        break