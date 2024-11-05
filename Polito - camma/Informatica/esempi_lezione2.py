lista = [3, 1, 2]

lista2 = lista[:] #crea una copia della lista

lista[0:1] = [5, 6] 
print(lista) # -> [5, 6, 2]

lista[0:1] = [] #posso anche restringere una lista in questo modo
print(lista) # -> [2]