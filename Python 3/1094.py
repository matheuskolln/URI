n = int(input())
c, r, s = 0, 0, 0

for i in range(0, n):
    q, e = input().split(' ')
    
    if e == 'C':
        c += int(q)
    elif e == 'R':
        r += int(q)
    elif e == 'S':
        s += int(q)

print('Total: {} cobaias'.format(c + r + s))
print('Total de coelhos: {}'.format(c))
print('Total de ratos: {}'.format(r))
print('Total de sapos: {}'.format(s))
print('Percentual de coelhos: {:.2f} %'.format(c / (c + r + s) * 100))
print('Percentual de ratos: {:.2f} %'.format(r / (c + r + s) * 100))
print('Percentual de sapos: {:.2f} %'.format(s / (c + r + s) * 100))