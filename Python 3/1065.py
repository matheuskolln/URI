c = 0
for x in range(0, 5):
	v = float(input())
	if v % 2 == 0:
		c += 1		
print('{} valores pares'.format(c))