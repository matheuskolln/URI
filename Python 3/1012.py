a, b, c = (input().split(' '))

tri = (float(a) * float(c)) / 2
cir = 3.14159 * (float(c) ** 2)
tra = ((float(a) + float(b)) * float(c)) / 2
qua = float(b) ** 2
ret = float(a) * float(b)

print('TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}'.format(tri, cir, tra, qua, ret))