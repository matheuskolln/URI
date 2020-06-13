n1, n2, n3, n4 = map(float, input().split(' '))

m = ((n1 * 2) + (n2 * 3) + (n3 * 4) + n4) / 10
print('Media: {:.1f}'.format(m))

if m >= 7:
    print('Aluno aprovado.')
elif m < 5:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    e = float(input())
    print('Nota do exame: {:.1f}'.format(e))
    mf = (e + m) / 2
    if mf >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: {:.1f}'.format(mf))