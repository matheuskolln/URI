x = int(input())
y = int(input())
s = []

if x > y:
    s = y
    y = x
    x = s
    s = []

for c in range(x+1, y):
    if c % 5 in (2, 3):
        s.append(c)

s = sorted(s)
for n in s:
    print(n)