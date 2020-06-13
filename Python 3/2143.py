while True:
    n = int(input())
    if not n:
        break
    p = []
    while n:
        n -= 1
        x = int(input())
        if x % 2 == 0:
            p.append((2 * x) - 2)
        else:
            p.append((2 * x) - 1)
    for i in p:
        print(i)     