def my_square(lato):
	return (lato**2, lato*4)

lato = float(input("Inserisci il lato del cubo:\n"))
quadrato = my_square(lato)

print(f"L'area del quadrato è: {quadrato[0]} il perimetro è: {quadrato[1]}")