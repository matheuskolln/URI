m, c = 0, 0
while True:
    i = int(input())
    if i < 0:
        break
    m += i
    c += 1
print('{:.2f}'.format(m / c))