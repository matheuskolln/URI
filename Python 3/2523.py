while True:
    try:
        r = input()
        q = int(input())
        p = [int(x) - 1 for x in input().split()] 
        for c in range(q):
            print(r[p[c]], end='')
        print()
    except EOFError:
        break