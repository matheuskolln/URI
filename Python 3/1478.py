while True:
    n = int(input())

    if n == 0:
        break

    r =  []

    for i in range(1, n + 1):
        tmp = []
        c = i
        for j in range(n):
            tmp.append(abs(c))
            if c == 1:
                c -= 3
            else:
                c -= 1
        r.append(tmp)

    for i in range(n):
        tx = ''
        for j in range(n):
            tx += " %3d" %r[i][j]
        print(tx[1:])
    print("")