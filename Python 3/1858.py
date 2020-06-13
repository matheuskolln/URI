n = int(input())
l = list(map(int, input().split(' ')))

for c in range(n):
    if min(l) == l[c]:
        print(c+1)
        break