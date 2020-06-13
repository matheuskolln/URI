m = []
o = input()

for i in range(0, 12):
    n = []
    for j in range(0, 12):
        x = float(input())
        n.append(x)
    m.append(n)

s = 0
k = 1
c = 0
for i in range(1, 11):
    for j in range(0, k):
        s += m[i][j]
        c += 1
    if i < 5:
        k += 1
    elif i > 5:
        k -= 1

if o == 'S':
    print('{:.1f}'.format(s))
elif o == 'M':
    print('{:.1f}'.format(s / c))