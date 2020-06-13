n = int(input())
for i in range(0, n):
    x = int(input())
    d = []
    for j in range(1, x+1):
        if x % j == 0:
            d.append(j)
    print('{} eh primo'.format(x) if len(d) == 2 else '{} nao eh primo'.format(x))
    d.clear()