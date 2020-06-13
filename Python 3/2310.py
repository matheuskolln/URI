n = int(input())
t_s, t_b, t_a = 0, 0, 0
s, b, a = 0, 0, 0
for c in range(n):
    name = input()
    ts, tb, ta = map(int, input().split(' '))
    sf, bf, af = map(int, input().split(' '))
    t_s += ts
    t_b += tb
    t_a += ta
    s += sf
    b += bf
    a += af

print('Pontos de Saque: {:.2f} %.\nPontos de Bloqueio: {:.2f} %.\nPontos de Ataque: {:.2f} %.'.format((s / t_s) * 100, (b / t_b) * 100, (a / t_a) * 100))