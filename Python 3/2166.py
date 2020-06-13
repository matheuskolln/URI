def r(n):
    if n == 0:
        return 2
    x = 2 + 1 / r(n - 1)
    return x

n = int(input())
x = r(n) - 1
print('{:.10f}'.format(x))