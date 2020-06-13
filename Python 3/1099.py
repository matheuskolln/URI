q = int(input())
l = []

for c in range(0, q):	
    x, y = map(int, input().split(' '))
    s = 0
    if x >= y:
        for n in range(y+1, x):
            if n % 2 != 0:
                s+= n
    else:
        for n in range(x+1, y):
            if n % 2 != 0:
                s+= n

    l.append(s)

for num in l:
	print(num)