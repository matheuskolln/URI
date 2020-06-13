n = int(input())
l = list(map(int, input().split(' ')))
m2, m3, m4, m5 = 0, 0, 0, 0
for c in range(n):
    if l[c] % 2 == 0:
        m2 += 1
    if l[c] % 3 == 0:
        m3 += 1
    if l[c] % 4 == 0:
        m4 += 1
    if l[c] % 5 == 0:
        m5 += 1

print('{} Multiplo(s) de 2\n{} Multiplo(s) de 3\n{} Multiplo(s) de 4\n{} Multiplo(s) de 5\n'.format(m2, m3, m4, m5), end='')