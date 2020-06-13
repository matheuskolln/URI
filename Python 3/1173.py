n = []
x = int(input())

while len(n) != 10:
    n.append(x)
    x *= 2

for i in range(len(n)):
    print('N[{}] = {}'.format(i, n[i]))