import numpy as np
mat = [[10,22,21,8,9],[9,42,3,18,11],[5,4,30,12,29],[37,31,7,2,26],[8,6,4,33,15]]

mat = np.array(mat)
min = mat.min()
max = mat.max()

mat = mat - min
mat = mat / (max-min)

print(mat)
