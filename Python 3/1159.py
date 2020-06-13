while True:
    x = int(input())
    if x == 0:
        break
    s = 0
    for c in range(x, x + 10):
        if c % 2 == 0:
            s += c
    print(s)