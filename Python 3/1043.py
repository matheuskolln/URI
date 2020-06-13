a, b, c = map(float, input().split(' '))

if abs(b - c) < a and a < b + c:
    print('Perimetro = {:.1f}'.format(a + b + c))
else:
    s = ((a + b) * c) / 2
    print('Area = {:.1f}'.format(s))