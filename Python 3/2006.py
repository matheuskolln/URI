t = int(input())
l = list(map(int, input().split(' ')))
cont = 0
for c in range(len(l)):
    if l[c] == t:
        cont += 1
print(cont)