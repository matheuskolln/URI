a, b, c, d = map(int, input().split(' '))
if abs(b - c) < a < b + c :
    print('S')
elif abs(b - c) < d < b + c:
    print('S')
elif abs(b - d) < a < b + d:
    print('S')
elif abs(c - d) < a < c + d:
    print('S')
else:
    print('N')