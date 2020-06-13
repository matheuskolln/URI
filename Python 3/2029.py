while True:
    try:
        vol = float(input())
        dia = float(input())
        alt = vol / (((dia / 2) ** 2) * 3.14)
        area = 3.14 * ((dia / 2) ** 2)
        print('ALTURA = {:.2f}'.format(alt))
        print('AREA = {:.2f}'.format(area))
    except EOFError:
        break
