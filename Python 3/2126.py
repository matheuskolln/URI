caso = 1
while True:
    try:
        sub = input()
        seq = input()
        cont = seq.count(sub)
        pos = seq.rfind(sub)
        print('Caso #{}:'.format(caso))
        if cont != 0:
            print('Qtd.Subsequencias: {}'.format(cont))
            print('Pos: {}'.format(pos + 1))
        else:
            print('Nao existe subsequencia')
        print()
        caso += 1
    except EOFError:
        break