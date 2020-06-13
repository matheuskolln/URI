x = int(input())
z = int(input())

while z <= x:
    z = int(input())

v, s = 0, 0
while s <= z:
    s += x+v
    v += 1
print(v)