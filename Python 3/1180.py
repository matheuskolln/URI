n = int(input())
l = [int(i) for i in input().split()]
if len(l) != n:
    for i in range(0, len(l) - n):
        l.pop()
m = min(l)
for c in range(0, len(l)):
    if l[c] == m:
        print('Menor valor: {}\nPosicao: {}'.format(l[c], c))