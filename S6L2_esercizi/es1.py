import numpy as np

mat = ([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]])
#SI tratta di una matrice 3x5, ovvero cinque colonne e tre righe. Ogni riga è di fatto una lista. Per accedere ad un elemento, per esempio l'elemento nella seconda riga, in quarta posizione
	
elem = mat[1][3]
print(elem)

mat = np.array(mat)
#ex di accesso a singoli elementi:
	
elem2 = mat[1,3] #Prenderà il valore come in precedenza
print(elem2)
elem2 = mat[:,2:]
print(elem2) #prenderà tutte le righe e dalla terza colonna alla quinta