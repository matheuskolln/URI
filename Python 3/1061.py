d1 = int(input().split()[1])
h1, m1, s1 = (int(x) for x in input("").split(" : "))
d2 = int(input().split()[1])
h2, m2, s2 = (int(x) for x in input("").split(" : "))

i = s1 + m1 * 60 + h1 * 3600 + d1 * 86400 
f = s2 + m2 * 60 + h2 * 3600 + d2 * 86400 

if i < f:
	t = f - i
	d = int(t / 86400)
	t = t % 86400
	h = int(t / 3600)
	t = t % 3600
	m = int(t / 60)
	t = t % 60
	s = t

print("{} dia(s)".format(d))
print("{} hora(s)".format(h))
print("{} minuto(s)".format(m))
print("{} segundo(s)".format(s))