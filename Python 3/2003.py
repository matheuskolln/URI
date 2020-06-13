while True:
    try:
        h = list(map(int, input().split(':')))
        a = h[0] * 60 + h[1] + 60 - 480
        print('Atraso maximo: {}'.format(a) if a > 0 else 'Atraso maximo: 0')
    except EOFError:
        break
