n = int(input())
l = list(map(int, input().split(' ')))

for c in range(1, n):
    if l[c] < l[c-1]:
        print(c + 1)
        break
    if c == n - 1:
        print(0)