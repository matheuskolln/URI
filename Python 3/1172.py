x = []

while len(x) != 10:
    n = int(input())
    x.append(n if n > 0 else 1)

for i in range(len(x)):
    print('X[{}] = {}'.format(i, x[i]))