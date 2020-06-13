n = int(input())
for c in range(0, n):
    x, y = map(int, input().split(' '))
    s = 0
    for i in range(x, x + 2 * y):
        if i % 2 != 0:
            s += i 
    print(s)