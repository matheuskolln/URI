cpar = 0
cneg = 0
cpos = 0
for x in range(0, 5):
	v = float(input())
	if v > 0:
		cpos += 1
	elif v < 0:
		cneg +=1
	if v % 2 == 0:
		cpar += 1
		
print('{} valor(es) par(es)\n{} valor(es) impar(es)\n{} valor(es) positivo(s)\n{} valor(es) negativo(s)'.format(cpar, (5 - cpar), cpos, cneg))