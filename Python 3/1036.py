a, b, c = map(float, input().split(' '))

d = (b**2 - 4 * a * c)
if d < 0 or a == 0:
    print('Impossivel calcular')
else:
    r1 = (-b + (d ** 0.5)) / (2 * a)
    r2 = (-b - (d ** 0.5)) / (2 * a)
    print('R1 = {:.5f}\nR2 = {:.5f}'.format(r1, r2))