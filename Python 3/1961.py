p, n = map(int, input().split(' '))
l = list(map(int, input().split()))
s = ''
for i in range(n-1):
    if l[i+1] - l[i] > p or l[i] - l[i+1] > p:
        s = 'GAME OVER'
        break
    else:
        s = 'YOU WIN'
print(s)