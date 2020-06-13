n = int(input())
for i in range(0, n):
    x = int(input())
    d = []
    for j in range(1, x):
        if x % j == 0:
            d.append(j)
    print('{} eh perfeito'.format(x) if sum(d) == x else '{} nao eh perfeito'.format(x))
    d.clear()