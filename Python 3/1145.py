x, y = map(int, input().split(' '))
c = 0 
for n in range(1, y + 1):
    c += 1
    if c != x:
        print(n, end=' ')
    if c == x:
        print(n)
        c = 0