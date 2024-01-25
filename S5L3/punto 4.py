#Punto 4
def massimo(x):
    z = x[0]
    for i in range(len(x)):
        if z < x[i]:
            z = x[i]
    return z

def minimo(x):
    z = x[0]
    for i in range(len(x)):
        if z > x[i]:
            z = x[i]
    return z

seq = [32, 35, 53, 2, 3, 40000, 5, 6, 52, 11, 122, 1222, 456, 31, 6790]
print(massimo(seq))
print(minimo(seq))
