while True:
    try:
        m, d = map(int, input().split(' '))
        a = [31,29,31,30,31,30,31,31,30,31,30,31]
        t = 0
        if m == 12:
            if d == 24:
                print('E vespera de natal!')
            elif d == 25:
                print('E natal!')
            elif d > 25:
                print('Ja passou!')
        else:
            for c in range(m - 1, 12):
                t += a[c]
            t -= d
            t -= 6
            print('Faltam {} dias para o natal!'.format(t))
    except EOFError:
        break