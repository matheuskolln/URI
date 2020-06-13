f = []
a, p, c = 0, 0, 0

while c <= 46:
    f.append(p)
    p += a
    a = p - a
    if p == 0:
        p += 1
    c += 1

n = int(input())
for x in range(0, n):
    if x == n - 1:
        print(f[x])
    else:
        print(f[x], end=' ')