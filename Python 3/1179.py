p = []
i = []
for c in range(0, 15):
    n = int(input())
    p.append(n) if n % 2 == 0 else i.append(n)
    if len(p) == 5:
        for y in range(0,5):
            print('par[{}] = {}'.format(y, p[y]))
        p.clear()
    if len(i) == 5:
        for z in range(0,5):
            print('impar[{}] = {}'.format(z, i[z]))
        i.clear()

for j in range(0,len(i)):
        print('impar[{}] = {}'.format(j, i[j]))
for k in range(0,len(p)):
        print('par[{}] = {}'.format(k, p[k]))