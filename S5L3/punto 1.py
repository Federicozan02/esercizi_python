#Punto 1
#N1
lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", "MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F", "DEFGHI95J06A987G"]
lista_res = list()
tester = "95"

for codice in lista_cf:
	if tester in codice:
		lista_res.append(codice)
		print ("Il nome è ", codice[0:3], "Il cognome è ", codice[3:6])

print(lista_res)

#N2
guadagni =[100,90,70,40,50,80,90,120,80,20,50,50]
sum =0
mesi = len(guadagni)
for guadagno in guadagni:
	sum +=guadagno

print(sum/mesi)

#N3
for numero in range(21): 
    print(numero)
