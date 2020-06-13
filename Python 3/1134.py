alc, gas, die = 0, 0, 0

while True:
    while True:
        x = int(input())
        if x in (1,2,3,4):
            break
    if x == 4:
        break
    elif x == 1:
        alc += 1
    elif x == 2:
        gas += 1
    else:
        die += 1

print('MUITO OBRIGADO\nAlcool: {}\nGasolina: {}\nDiesel: {}'.format(alc, gas, die))