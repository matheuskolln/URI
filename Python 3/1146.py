while True:
    x = int(input())
    if x == 0:
        break
    for n in range(1, x+1):
        if n == x:
            print(n)
        else:
            print(n, end=' ')