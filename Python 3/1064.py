c = 0
m = 0
for x in range(0, 6):
	v = float(input())
	if v > 0:
		c += 1
		m += v
		
print('{} valores positivos\n{:.1f}'.format(c, m/c))