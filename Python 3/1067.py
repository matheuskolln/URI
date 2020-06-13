x = int(input())

if 1 <= x <= 1000:
	for n in range(0,x+1):
		if n % 2 != 0:
			print(n)