m = []
o = input()

for i in range(0, 12):
    n = []
    for j in range(0, 12):
        x = float(input())
        n.append(x)
    m.append(n)

s = 0
b = 1
a = 11
c = 0
for i in range(0, 5):
    for j in range(b, a):
        s += m[i][j]
        c += 1
    b += 1
    a -= 1

if o == 'S':
    print('{:.1f}'.format(s))
elif o == 'M':
    print('{:.1f}'.format(s / c))