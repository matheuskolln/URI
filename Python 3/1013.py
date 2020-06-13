a, b, c = (input().split(' '))

m = (int(a)+int(b)+abs(int(a)-int(b))) / 2
n = (int(m)+int(c)+abs(int(m)-int(c))) / 2

print('{} eh o maior'.format(int(n)))