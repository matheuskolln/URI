t = int(input())
for c in range(0, t):
    pa, pb, ca, cb = map(float, input().split(' '))
    a = 0
    while pa <= pb:
        a += 1
        pa += int(pa * (ca / 100))
        pb += int(pb * (cb / 100))
        if a > 100:
            break
    print('Mais de 1 seculo.' if a > 100 else '{} anos.'.format(a))