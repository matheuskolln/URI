q = int(input())
t = 0

for c in range(q):
    n, v = map(int, input().split(' '))
    if n == 1001:
        t += v * 1.5
    elif n == 1002:
        t += v * 2.5
    elif n == 1003:
        t += v * 3.5
    elif n == 1004:
        t += v * 4.5
    elif n == 1005:
        t += v * 5.5

print('{:.2f}'.format(t))