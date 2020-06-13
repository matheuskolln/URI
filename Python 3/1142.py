n = int(input())
v = []
k = 0

for c in range(1, 4*n):
    if c % 4 != 0:
        v.append(c)

for x in range(0, len(v)):
    print(v[x], end=' ')
    k += 1 
    if k == 3:
        print('PUM')
        k = 0