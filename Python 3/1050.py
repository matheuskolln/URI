n = int(input())
d = [61, 71, 11, 21, 32, 19, 27, 31]
c = ['Brasilia', 'Salvador', 'Sao Paulo', 'Rio de Janeiro', 'Juiz de Fora', 'Campinas', 'Vitoria', 'Belo Horizonte']
a = 0

if n not in d:
	print('DDD nao cadastrado')

for x in d:
	if n == x:
		print(c[a])
	a += 1