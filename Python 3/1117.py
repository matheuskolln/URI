m, c = 0, 0

while True:
    if c == 2:
        break
    else:
        n = float(input())
        if 0 <= n <= 10:
            c += 1
            m += n
        else:
            print('nota invalida')
            
print('media = {:.2f}'.format(m/2))