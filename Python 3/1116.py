n = int(input())
for c in range(0, n):
    x, y = map(int, input().split(' '))
    try:
        print('{:.1f}'.format(x / y))
    except:
        print('divisao impossivel')