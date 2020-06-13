while True:
    n = int(input())
    if (n == 0):
        break
    r =  []
    for i in range(n):
        tmp = []
        for j in range(n):
            tmp.append(1)
        r.append(tmp)

    v, c, e, b, d = 1, 0, 0, n - 1, n - 1

    if n % 2 == 0:
        m = n / 2
    else:
        m = (n + 1) / 2

    while v <= m:
        i = e
        while (i <= d):
            r[c][i] = v
            r[b][i] = v
            i+=1

        i = (c + 1)
        while ( i < b):
            r[i][e] = v
            r[i][d] = v
            i+=1

        v+=1
        c+=1
        b-=1
        e+=1
        d-=1

    for i in range(n):

        for j in range(n):
            if j == n - 1:
                print("%3d" %r[i][j])
            else:
                print("%3d" %r[i][j],end=' ')
    print('')