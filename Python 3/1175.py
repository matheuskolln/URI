n = []
aux = 0
while len(n) != 20:
    x = int(input())
    n.append(x)

for c in range (0, 10):
    aux = n[c]
    n[c] = n[-c-1]
    n[-c-1] = aux

for i in range(len(n)):
    print('N[{}] = {}'.format(i, n[i]))