f = []
a, p = 0, 0

while len(f) <= 60:
    f.append(p)
    p += a
    a = p - a
    if p == 0:
        p += 1

x = int(input())
for n in range(x):
    t = int(input())
    print('Fib({}) = {}'.format(t, f[t]))