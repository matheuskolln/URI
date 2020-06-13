s = 0
o = input()
for i in range(11, -1, -1):
    for j in range(0, 12):
        x = float(input())
        if j < i:
            s += x

if o == 'S':
    print('{:.1f}'.format(s))
elif o == 'M':
    print('{:.1f}'.format(s / 66))