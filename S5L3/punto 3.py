#Punto 3
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie": "Golf", "Debbie": "107", "Emily": "A1"} 
nuovi_proprietari = {"Ben": "Polo", "Fred": "Octavia", "Grace": "Yaris", "Hugh": "Clio"}

for i in nuovi_proprietari.keys():
	dizionario_auto[i] = nuovi_proprietari[i]
	
print(dizionario_auto)
#Il valore della macchina di ben è stato sostituito con quella di nuovi proprietari
