p, j1, j2, r, a = map(int, input().split(' '))
w = 0
n = j1 + j2

if r == 1:
    if a == 1:
        w = 2
    else:
        w = 1
elif p == 1:
    if n % 2 == 0:
        w = 1
    else:
        w = 2
elif p == 0:
    if n % 2 != 0:
        w = 1
    else:
        w = 2

print('Jogador 1 ganha!' if w == 1 else 'Jogador 2 ganha!')