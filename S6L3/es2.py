import pandas as pd

csv_nam = ("iris.data")

nomi = (["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)", "class"])
data = pd.read_csv("iris.data", header = None, delimiter = ',', names = nomi)

matrice = pd.DataFrame(data)
print(matrice.head(5)) #primi 5
print("I nomi di colonna sono: ", data.columns) # nomi delle colonne
print(matrice.tail(10)) # ultimi 10
print(matrice.describe()) #stats
