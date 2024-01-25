import numpy as np

def crivello (n, limite):
	numeriTot = np.arange(2,limite+1)
	primi = []
	while len(primi) < n:
		valut = numeriTot[0]
		primi.append(valut)
		numeriTot = np.delete(numeriTot, np.where(numeriTot % valut == 0))
	
	return primi

n = int(input("Inserire un numero: "))
limite = int(input("Inserire il limite: "))
print(crivello(n, limite))

    	
