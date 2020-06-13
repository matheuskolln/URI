n, a = map(int, input().split(' '))
for c in range(a):
    x = input()
    if x == 'fechou':
        n += 1
    elif x == 'clicou':
        n -= 1
print(n)