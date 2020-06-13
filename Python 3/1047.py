x, x1, y, y1 = map(int, input().split(' '))

i = x * 60 + x1
f = y * 60 + y1

if (f > i):
    m = f - i
else:
    m = (24 * 60) - i + f

h = m // 60
m = m % 60

if h == 0 and m == 0:
	h = 24
	m = 0

print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(h, m))