while True:
    try:
        n = int(input())
        l = list(map(int, input().split(' ')))
        if max(l) < 10:
            print('1')
        elif 10 <= max(l) < 20:
            print('2')
        else:
            print('3')
    except EOFError:
        break