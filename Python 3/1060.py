c = 0

for x in range(0, 6):
	v = float(input())
	if v > 0:
		c += 1
		
print('{} valores positivos'.format(c))