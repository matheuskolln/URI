n = int(input())
m = []
for i in range(0, n):
	a, b, c = map(float, input().split(' '))
	m.append((a * 2 + b * 3 + c * 5) / 10)
for j in m:
	print('{:.1f}'.format(j))