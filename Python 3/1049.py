x = input()
y = input()
z = input()

if x == 'vertebrado':
	if y == 'ave':
		if z == 'carnivoro':
			s = 'aguia'
		else:
			s = 'pomba'
	else:
		if z == 'onivoro':
			s = 'homem'
		else:
			s = 'vaca'
else:
	if y == 'inseto':
		if z == 'hematofago':
			s = 'pulga'
		else:
			s = 'lagarta'
	else:
		if z == 'hematofago':
			s = 'sanguessuga'
		else:
			s = 'minhoca'

print(s)