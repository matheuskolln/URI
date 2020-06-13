n = []
x = float(input())

while len(n) < 100:
    n.append(x)
    x /= 2

for c in range(0, len(n)):
    print('N[{}] = {:.4f}'.format(c, n[c]))