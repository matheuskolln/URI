n = int(float(input("")) * 100)
cs = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]
name = "nota"

print("NOTAS:")
for c in cs:
    if (c == 100):
        print("MOEDAS:")
        name = "moeda"
    print("{} {}(s) de R$ {:.2f}".format(int(n/c), name, c/100))
    n %= c