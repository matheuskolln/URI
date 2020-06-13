while True:
    x, y = map(int, input().split(' '))

    if x == y:
        break
    else:
        print('Crescente' if x < y else 'Decrescente')