#Punto 5
def num_grand(x):
    if len(x) < 3:
        print("La lista è troppo corta")
    else:
        i = 0
        x.sort()
        x.reverse()
        while i < len(x) - 1:
            if x[i] == x[i + 1]:
                x.remove(x[i])
            else:
                i += 1
        if len(x) <= 3:
        	print("Il numero di elementi nella lista è giusto, ma ci sono troppi numeri uguali")
        else: 
            print("Gli elementi più grandi sono:", x[0:3])

seq1 =[327777,31,32920,11,1873,23,84,1873,341,1873,319,111,32920,2,327777]
num_grand(seq1)
