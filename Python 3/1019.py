s = int(input())

h = int(s / 3600)
m = int(s / 60) - h * 60
s = s - h * 3600 - m * 60

print('{}:{}:{}'.format(h, m, s))