s, t, f = map(int, input().split(' '))
if s == 0:
    s = 24
h = s + t + f
if h >= 24:
    h -= 24
print(h)