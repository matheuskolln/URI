l = input().split(' ')
s, a, n, c = 0, 0, 0, 0

while a == 0 or n == 0:
    if int(l[c]) > 0:
        if a == 0:
            a = int(l[c])
        elif n == 0:
            n = int(l[c])
    c += 1

for c in range(0, n):
    s += a + c

print(s)