m = []
o = input()

for i in range(0, 12):
    n = []
    for j in range(0, 12):
        x = float(input())
        n.append(x)
    m.append(n)

s = 0
c = 1
for i in range(0, 11):
    for j in range(c, 12):
        s += m[i][j]
    c += 1
if o == 'S':
    print('{:.1f}'.format(s))
elif o == 'M':
    print('{:.1f}'.format(s / 66))