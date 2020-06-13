while True:
    s = int(input())
    print('Acesso Permitido' if s == 2002 else 'Senha Invalida')
    if s == 2002:
        break