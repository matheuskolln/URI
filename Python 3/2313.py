l = list(map(int, input().split(' ')))
l.sort()

a, b, c = l

if a + b <= c:
    print("Invalido")
else:
    if a == b and b == c:
        t = "Valido-Equilatero"
    elif a == b or b == c:
        t = "Valido-Isoceles"
    else:
        t = "Valido-Escaleno"
    if (a ** 2) + (b ** 2) == c ** 2:
        r = 'S'
    else:
        r = 'N'
    print(t)
    print("Retangulo:", r)