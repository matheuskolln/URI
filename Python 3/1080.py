m, p = 0, 0

for i in range(100):
	n = int(input())
	if n > m:
		m, p = n, i

print('{}\n{}'.format(m, p+1))