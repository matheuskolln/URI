n = int(input())
for c in range(n):
    h, m, o = map(int, input().split(' '))
    r = ''

    if h < 10 and len(str(h)) == 1:
        r = '0' + str(h)
    else:
        r = str(h)

    r += ':'

    if m < 10 and len(str(m)) == 1:
        r += '0' + str(m)
    else:
        r += str(m)

    r += ' - A porta '

    if o == 0:
        r += 'fechou!'
    else:
        r += 'abriu!'

    print(r)