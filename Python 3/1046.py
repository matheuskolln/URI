x, y = map(int, input().split(' '))

if x >= y:
	h = 24 - x + y
else:
	h = y - x

print('O JOGO DUROU {} HORA(S)'.format(h))