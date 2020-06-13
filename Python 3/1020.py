d = int(input())

a = int(d / 365)
m = int(d % 365 / 30)
d = d % 365 % 30

print('{} ano(s)\n{} mes(es)\n{} dia(s)'.format(a, m , d))