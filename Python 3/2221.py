n = int(input())
for c in range(n):
    b = int(input())
    a1, d1, l1 = map(int, input().split(' '))
    a2, d2, l2 = map(int, input().split(' '))

    g1 = (a1 + d1) / 2.0
    g2 = (a2 + d2) / 2.0

    if l1 % 2 == 0:
        g1 += b
    if l2 % 2 == 0:
        g2 += b

    if g1 > g2:
        print('Dabriel')
    elif g2 > g1:
        print('Guarte')
    else:
        print('Empate')