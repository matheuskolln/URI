from math import log

n = int(input())

menor = n / log(n)
maior = 1.25506 * (n / log(n))

print('{:.1f} {:.1f}'.format(menor, maior))