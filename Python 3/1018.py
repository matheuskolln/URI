v = t = int(input())
n100 = n50 = n20 = n10 = n5 = n2 = n1 = 0

while v != 0:
    if v/100 >= 1:
        v -= 100
        n100 += 1
    elif v/50 >= 1:
        v -= 50
        n50 += 1
    elif v/20 >= 1:
        v -= 20
        n20 += 1
    elif v/10 >= 1:
        v -= 10
        n10 += 1
    elif v/5 >= 1:
        v -= 5
        n5 += 1
    elif v/2 >= 1:
        v -= 2
        n2 += 1
    elif v/1 >= 1:
        v -= 1
        n1 += 1
print(t)
print('{} nota(s) de R$ 100,00'.format(n100))
print('{} nota(s) de R$ 50,00'.format(n50))
print('{} nota(s) de R$ 20,00'.format(n20))
print('{} nota(s) de R$ 10,00'.format(n10))
print('{} nota(s) de R$ 5,00'.format(n5))
print('{} nota(s) de R$ 2,00'.format(n2))
print('{} nota(s) de R$ 1,00'.format(n1))