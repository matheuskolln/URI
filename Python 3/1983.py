q = int(input())
a, na = [], []
for c in range(q):
    m, n = map(float, input().split(' '))
    a.append(m)
    na.append(n)
if max(na) < 8:
    print('Minimum note not reached')
else:
    for c in range(q):
        if max(na) == na[c]:
            print(int(a[c]))
