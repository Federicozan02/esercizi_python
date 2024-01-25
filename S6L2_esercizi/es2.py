import numpy as np

linear_data = np.array([x for x in range(27)])
reshaped_data = linear_data.reshape((3, 3, 3))

print (linear_data.shape)
print (reshaped_data.shape)
#Il nuovo array è una matrice 3x3x3 alla quale possiamo accedervi:
	
print (reshaped_data[2,2,2]) #singolo valore
print (reshaped_data[0,:,1:]) #più valori