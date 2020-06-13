s = float(input())

if s <= 2000:
	i = 'Isento'
else:
	i = 0
	if s <= 3000:
		i += (s - 2000) * 0.08
	if 3000 < s <= 4500:
		i += (s - 3000) * 0.18 + 1000 * 0.08
	if s > 4500:
		i += (s - 4500) * 0.28 + 1500 * 0.18 + 1000 * 0.08
	i = 'R$ {:.2f}'.format(i)

print(i)