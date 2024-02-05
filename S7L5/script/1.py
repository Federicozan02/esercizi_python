import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


def zScore(data):
    media = np.mean(data)
    dev = np.std(data)
    return (data - media) / dev


def boxplot(nome):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=dati[nome], color="skyblue")
    plt.title(f'Boxplot della distribuzione per {nome}')
    plt.show()


def hist(nome):
    plt.figure(figsize=(10, 6))
    sns.histplot(dati[nome], color="darkgreen")
    plt.title(f'Distribuzione per {nome}')
    plt.show()
    

file_name = "dataset_climatico.csv"
clima = pd.read_csv(file_name)

dati = pd.DataFrame(clima)

# Rimozione valori nulli
dati.dropna(inplace=True)

dati["temperatura_media"] = zScore(dati["temperatura_media"])
dati["umidita"] = zScore(dati["umidita"])
dati["precipitazioni"] = zScore(dati["precipitazioni"])
dati["velocita_vento"] = zScore(dati["velocita_vento"])


boxplot('temperatura_media')
boxplot('umidita')
boxplot('precipitazioni')
boxplot('velocita_vento')

hist('temperatura_media')
hist('umidita')
hist('precipitazioni')
hist('velocita_vento')
