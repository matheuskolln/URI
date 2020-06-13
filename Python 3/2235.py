x, y, z = map(int, input().split(' '))

if x == y or x == z or y == z:
    print('S')
elif x + y == z or x + z == y or z + y == x:
    print('S')
else:
    print('N')