def r(n):
    if n == 0:
        return 6
    x = 6 + 1 / r(n - 1)
    return x

n = int(input())
x = r(n) - 3
print('{:.10f}'.format(x))