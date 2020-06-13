x = int(input())
y = int(input())
s = 0

for n in range(y+1, x):
	if n % 2 != 0:
		s+= n

print(s)