n = int(input())
l = map(int, input().split())
pos, som, tot, run = 0, 0, 0, True

for i, j in enumerate(l):
    tot += j
    if j % 2 == 0 and run:
        atk = i + 1
        som += ((i * 2) + 1) - pos
        run = False
    if j - 1 == 0 and run:
        pos = i + 1

else:
    if som > 0:
        tot -= som
    else:
        atk = n
        tot -= atk

print("{} {}".format(atk,tot))