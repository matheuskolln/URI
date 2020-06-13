n = int(input())

def s(n):
    u = n % 10

    n //= 10
    d = n % 10

    n//= 10
    c = n % 10
    return c,d,u

def r(c,d,u):
    txt =''
    if c > 0:
        if c <= 3:
            txt += 'C'*(c)
        elif c == 4:
            txt += 'CD'
        elif c == 5:
            txt += 'D'
        elif c > 5 and c < 9:
            txt += 'D' + 'C'*(c-5)
        elif c == 9:
            txt += 'CM'

    if d > 0:
        if d <= 3:
            txt += 'X'*(d)
        elif d == 4:
            txt += 'XL'
        elif d == 5:
            txt += 'L'
        elif d > 5 and d < 9:
            txt += 'L' + 'X'*(d-5)
        elif d == 9:
            txt += 'XC'
    if u > 0:
        if u <= 3:
            txt += 'I'*(u)
        elif u == 4:
            txt += 'IV'
        elif u == 5:
            txt += 'V'
        elif u > 5 and u < 9:
            txt += 'V' + 'I'*(u-5)
        elif u == 9:
            txt += 'IX'


    return txt

def main():
    c,d,u = s(n)
    print(r(c,d,u))

main()