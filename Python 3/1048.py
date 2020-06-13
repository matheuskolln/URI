s = float(input())

if s <= 400:
	p = '15 %'
	r = 0.15 * s
	s += r
elif 400 < s <= 800:
	p = '12 %'
	r = 0.12 * s
	s += r
elif 800 < s <= 1200:
	p = '10 %'
	r = 0.10 * s
	s += r
elif 1200 < s <= 2000:
	p = '7 %'
	r = 0.07 * s
	s += r
else: 
	p = '4 %'
	r = 0.04 * s
	s += r 

print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {}'.format(s, r, p))