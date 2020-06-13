a, b = input().split(' ')
x, y = input().split(' ')

d = (((float(x) - float(a))**2) + ((float(y) - float(b))**2)) ** 0.5

print('{:.4f}'.format(d))