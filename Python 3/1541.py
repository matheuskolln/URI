while True:
    n = [int(x) for x in input().split(' ')]

    if n[0] == 0: 
        break

    a = n[0] * n[1]
    i = 0

    while i * i * n[2] / 100 <= a:
        i += 1
    
    print(i - 1)