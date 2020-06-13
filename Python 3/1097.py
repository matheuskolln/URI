i, j = 1, 7

while i <= 9:
    for c in range(0, 3):
        print('I={} J={}'.format(i, j))
        j -= 1
    i += 2
    j += 5