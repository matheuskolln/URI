while True:
    n, m = map(int, input().split(' '))
    if n == m == 0:
        break
    tr = m - n
    cont = 0

    while tr != 0:
        if tr < 2:
            break
        if tr / 100 >= 1:
            tr -= 100
        elif tr / 50 >= 1:
            tr -= 50    
        elif tr / 20 >= 1:
            tr -= 20
        elif tr / 10 >= 1:
            tr -= 10
        elif tr / 5 >= 1:
            tr -= 5
        elif tr / 2 >= 1:
            tr -= 2
        cont += 1

    if cont == 2:
        print('possible')
    else:
        print('impossible')