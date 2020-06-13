i , j = 0, 1

while i <= 2:
    for c in range (0, 3):
        if i == 1.0 or i == 0.0 or i > 1.8: 
            print('I={:.0f} J={:.0f}'.format(i,j))
        else:
            	print('I={:.1f} J={:.1f}'.format(i, j))
        j += 1
    i += 0.2
    j = i + 1