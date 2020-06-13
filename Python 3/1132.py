x = int(input())
y = int(input())
s = 0

if x > y:
    s = y
    y = x
    x = s
    s = 0

for c in range(x, y+1):
    if c % 13 != 0:
        s += c

print(s)