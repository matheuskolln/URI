m = []
c = int(input())
t = input()

for i in range(0, 12):
    n = []
    for j in range(0, 12):
        x = float(input())
        n.append(x)
    m.append(n)

s = 0
for j in range(0, 12):
    s += m[j][c]
    
if t == 'S':
    print('{:.1f}'.format(s))
elif t == 'M':
    print('{:.1f}'.format(s / 12))