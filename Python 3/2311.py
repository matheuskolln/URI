n = int(input())

for c in range(n):
    p = input()
    g = float(input())
    l = list(map(float, input().split(' ')))

    l.remove(min(l))
    l.remove(max(l))

    y = sum(l) * g

    print('{} {:.2f}'.format(p, y))