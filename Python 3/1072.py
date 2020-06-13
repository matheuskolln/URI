n = int(input())
vin = vout = 0
x = [num for num in range(10,21)]

for v in range(0, n):
	a = int(input())
	if a in x:
		vin +=1
	else:
		vout +=1

print('{} in\n{} out'.format(vin, vout))