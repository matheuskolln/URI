gre, inte, emp, quant, x = 0, 0, 0, 0, 1

while x == 1:
    i, g = map(int, input().split(' '))
    while True:
        print('Novo grenal (1-sim 2-nao)')
        x = int(input())
        if x in (1,2):
            break
    if i > g:
        inte += 1
    elif i < g:
        gre += 1
    else:
        emp += 1
    quant += 1

print('{} grenais\nInter:{}\nGremio:{}\nEmpates:{}'.format(quant, inte, gre, emp))
if inte > gre:
    print('Inter venceu mais')
elif gre > inte:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')