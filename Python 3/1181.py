m = []
l = int(input())
t = input()

for i in range(0, 12):
    n = []
    for j in range(0, 12):
        x = float(input())
        n.append(x)
    m.append(n)

if t == 'S':
    print('{:.1f}'.format(sum(m[l])))
elif t == 'M':
    print('{:.1f}'.format(sum(m[l]) / 12))