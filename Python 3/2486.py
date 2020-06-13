while True:
    t = int(input())
    if t == 0:
        break
    c = 0 
    for j in range(t):
        l = list(input().split(' '))
        q, p = l[0], l[1]
        if p == 'suco':
            c += int(q) * 120
        elif p == 'morango':
            c += int(q) * 85
        elif p == 'mamao':
            c += int(q) * 85
        elif p == 'goiaba':
            c += int(q) * 70
        elif p == 'manga':
            c += int(q) * 56
        elif p == 'laranja':
            c += int(q) * 50
        elif p == 'brocolis':
            c += int(q) * 34
    if c > 130:
        print('Menos {} mg'.format(c - 130))
    elif c < 110:
        print('Mais {} mg'.format(110 - c))
    else:
        print('{} mg'.format(c))