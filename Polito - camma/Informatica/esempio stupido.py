altezza = int(input("Inserisci l'altezza dell'albero di natale:\n"))
# while altezza > 10 or altezza <= 0 or not altezza.isdigit():
while altezza > 10 or altezza <= 0:
	print("Bestia")
	altezza = int(input("Reinserisci l'altezza dell'albero di natale:\n"))

h = altezza * 2 + 1
for i in range(1, h, 2):
	s = i * "*"
	print(f"{s:^{h-1}}")

