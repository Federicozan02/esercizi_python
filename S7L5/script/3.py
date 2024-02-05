import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


file_name = "dataset_climatico.csv"
clima = pd.read_csv(file_name)

dati = pd.DataFrame(clima)
d1 = pd.DataFrame(dati[['temperatura_media', 'precipitazioni', 'umidita', 'velocita_vento']])

matrice_correlazione = d1.corr()
sns.heatmap(matrice_correlazione, annot=True, cmap="coolwarm")
plt.title("Matrice di Correlazione")
plt.show()
