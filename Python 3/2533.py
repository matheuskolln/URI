while True:
    try:
        n = int(input())
        a = 0
        b = 0
        for c in range(n):
            n, c = map(int, input().split(' '))
            a += n * c
            b += c
        print('{:.4f}'.format(a / (b * 100)))
    except EOFError:
        break