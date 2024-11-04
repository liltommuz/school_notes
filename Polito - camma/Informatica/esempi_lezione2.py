l = []

def fact(n):
	
	
	if n != 1:
		l.append(n)
		n = n * fact(n-1)
		
		print(l)
	return n

print(fact(997))
