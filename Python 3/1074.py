n = int(input())
cs = []
for x in range(0, n):
	v = int(input())
	if v != 0:
		if v % 2 == 0 :
			c1 = 'EVEN'
		else:
			c1 = 'ODD'
		if v > 0:
			c2 = 'POSITIVE'
		else:
			c2 = 'NEGATIVE'
		cs.append('{} {}'.format(c1, c2))
	else:
		cs.append('NULL')
for c in cs:
	print(c)