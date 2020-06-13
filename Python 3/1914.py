n = int(input())
for c in range(0, n):
    p1, o1, p2, o2 = input().split(' ')
    n1, n2 = map(int, input().split(' '))

    if o1 == 'PAR' and (n1 + n2) % 2 == 0:
        print(p1) 
    elif o1 == 'IMPAR' and (n1 + n2) % 2 == 0:
        print(p2) 
    elif o1 == 'IMPAR' and (n1 + n2) % 2 != 0:
        print(p1) 
    elif o1 == 'PAR' and (n1 + n2) % 2 != 0:
        print(p2) 