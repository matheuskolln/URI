c, q = map(int, input().split(' '))
p = [0, 4, 4.5, 5, 2, 1.5]

v = p[c] * q
print('Total: R$ {:.2f}'.format(v))