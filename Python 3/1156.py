s, c, x = 0, 1, 1
while c <= 39:
    s += c/x
    c += 2
    x *= 2
print('{:.2f}'.format(s))