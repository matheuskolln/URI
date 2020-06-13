m = []
o = input()

for i in range(0, 12):
    n = []
    for j in range(0, 12):
        x = float(input())
        n.append(x)
    m.append(n)

s = 0
c = 11
for i in range(11, 0, -1):
    for j in range(0, c):
        s += m[i][j]
    c -= 1

if o == 'S':
    print('{:.1f}'.format(s))
elif o == 'M':
    print('{:.1f}'.format(s / 66))