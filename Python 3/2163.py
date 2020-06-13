lin, col = map(int, input().split(' '))

m = list() 

for i in range(lin):                               
    m.append( [int(col_i) for col_i in input().split()] )  

t = t2 = 0
ok = False

for i in range(1, lin-1):
    if ok:
        break

    for j in range(1, col-1):
        if m[i][j] == 42:
            if m[i-1][j-1] == 7 and m[i-1][j] == 7 and m[i-1][j+1] == 7:
                if m[i][j-1] == 7 and m[i][j + 1] == 7:
                    if m[i+1][j-1] == 7 and m[i+1][j] == 7 and m[i+1][j+1] == 7:
                        t = i+1
                        t2 = j+1
                        ok = True
                        break

print("{} {}".format(t, t2))