n = []
t = int(input())

while len(n) < 1000:
    for c in range(0, t):
        if len(n) < 1000:
            n.append(c)

for i in range(len(n)):
    print('N[{}] = {}'.format(i, n[i]))