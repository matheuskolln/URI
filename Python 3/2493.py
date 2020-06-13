from sys import stdin

class Expression:
    def __init__(self, n1, n2, result):
        self.n1 = n1
        self.n2 = n2
        self.result = result

def main():
    for line in stdin:
        t = int(line)
        ls = []
        for _ in range(t):
            vals, res = input().split('=')
            n1, n2 = map(int, vals.split())
            res = int(res)
            ls.append(Expression(n1, n2, res))
        names = []
        for _ in range(t):
            n, e, r = input().split()
            e = int(e) - 1
            add = ls[e].n1 + ls[e].n2 == ls[e].result
            sub = ls[e].n1 - ls[e].n2 == ls[e].result
            mul = ls[e].n1 * ls[e].n2 == ls[e].result
            imp = not (add or sub or mul)
            if r == '+': ans = add
            if r == '-': ans = sub
            if r == '*': ans = mul
            if r == 'I': ans = imp
            if not ans:
                names.append(n)
        if not names:
            print("You Shall All Pass!")
        elif len(names) == t:
            print("None Shall Pass!")
        else:
            names.sort()
            sz = len(names)
            for i in range(sz):
                print(names[i], end=(' ' if i < sz - 1 else '\n'))
    
if __name__ == "__main__":
    main()