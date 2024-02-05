import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


file_name = "dataset_climatico.csv"
clima = pd.read_csv(file_name)

dati = pd.DataFrame(clima)

d1 = pd.DataFrame(dati[['temperatura_media', 'precipitazioni', 'umidita', 'velocita_vento']])
#Rimozione valori nulli
dati.dropna(inplace = True)

print("La media è:")
print(np.mean(dati[["temperatura_media", "umidita", "velocita_vento", "precipitazioni"]], axis = 0))
print("La mediana è: ")
print(dati[["temperatura_media", "umidita", "velocita_vento", "precipitazioni"]].median(axis=0))
print("La deviazione standard è: ")
print(np.std(dati[["temperatura_media", "umidita", "velocita_vento", "precipitazioni"]], axis = 0))
