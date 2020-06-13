a = []

while len(a) != 100:
    x = float(input())
    a.append(x)

for i in range(len(a)):
    if a[i] <= 10:
        print('A[{}] = {:.1f}'.format(i, a[i]))