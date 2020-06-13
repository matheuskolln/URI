a, b, c = map(float, input().split(' '))
aux = 0

if a < c:
	aux = a
	a = c 
	c = aux

if a < b:
	aux = a
	a = b
	b = aux

if a >= b + c:
	print('NAO FORMA TRIANGULO')
else:
	if a ** 2 == b ** 2 + c ** 2:
		print('TRIANGULO RETANGULO')
	if a ** 2 > b ** 2 + c ** 2:
		print('TRIANGULO OBTUSANGULO')
	if a ** 2 < b ** 2 + c ** 2:
		print('TRIANGULO ACUTANGULO')
	if a == b == c:
		print('TRIANGULO EQUILATERO')
	if a == b != c or a == c != b or b == c != a:
		print('TRIANGULO ISOSCELES')