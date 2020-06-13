from math import sqrt
n = int(input())

f = (((1 + sqrt(5)) / 2) ** n - ((1 - sqrt(5)) / 2) ** n) / sqrt(5)
print('{:.1f}'.format(f))