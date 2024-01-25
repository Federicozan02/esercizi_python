def funz():
	k = int(input("Inserire un numero: "))
	lista = list()
	lista2 = list()
	
	for i in range(10):
		numero = int(input("Inserire il numero della sequenza: "))
		lista.append(numero)
	
	for j in range(10):
		if k <= lista[j]:
			lista2.append(lista[j])
			
	if len(lista2) == 0:
		print("I numeri inseriti sono tutti minori di 5")
	else:
	  print(sum(lista2)/len(lista2))
	
funz()
