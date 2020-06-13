m, x, i = 0, 1, 0
while x == 1:
    while i < 2:
        n = float(input())
        if 0 <= n <= 10:
            m += n
            i += 1
        else:
            print('nota invalida')
    print('media = {:.2f}'.format(m / 2))

    while True:
        print('novo calculo (1-sim 2-nao)')
        x = float(input())
        i = 0
        m = 0
        if x in (1, 2):
            break