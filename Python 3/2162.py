q = int(input())
l = list(map(int, input().split(' ')))

if q == 2 and l[0] == l[1]:
    p = 0
else:
    p = 1
    for i in range(1, q-1):
        if not ((l[i] < l[i-1] and l[i] < l[i+1]) or (l[i] > l[i-1] and l[i] > l[i+1])):
            p = 0
            break
print(p)