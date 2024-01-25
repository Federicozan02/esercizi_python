import pandas as pd

file_name = "wine.csv"

data = pd.read_csv(file_name) 
print(data)

#Describe ci permette di ottenere automaticamente delle rapide analisi statistiche,
#come conteggio, media, quartili, minimo e massimo.
stats = data.describe() 
moda = data.mode(axis = 0, numeric_only = True)
print (moda.iloc[0])
print (stats)
