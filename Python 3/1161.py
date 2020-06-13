a = []
s = 1
a.append(1)
for i in range(1,21):
    s *= i
    a.append(s)
try:
    while True:
        n, m = map(int, input().split(' '))
        print(a[n]+a[m])

except EOFError:
    pass