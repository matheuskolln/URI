while True:
    try:
        n = int(input())
        m = list()
        for i in range(n):
            m.append([])
            for j in range(n):
                m[i].append('0')
        for i in range(n):
            m[i][i] = '2'
        for i in range(n):
            m[i][n - 1 - i] = '3'
        for i in range(n // 3,n - n // 3):
            for j in range(n // 3,n - n // 3):
                m[i][j] = '1'
        m[n // 2][n // 2] = '4'
        for i in range(n):
            M = ''.join(m[i])
            print(M)
        print('')
    except EOFError:
        break