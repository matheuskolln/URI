while True:
    m, n = sorted([int(x) for x in input().split(' ')]), 0

    if m[0] <= 0 or m[1] <= 0:
        break

    for i in range(m[0], m[1] + 1):
        n += i
        if i == m[1]:
            print('{} Sum={}'.format(i, n))
        else:
            print(i, end=" ")