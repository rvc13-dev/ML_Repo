import numpy as np
#creating vector of size =15  with integers in range 1-20
input_array = np.random.randint(1,21, size=15)
#print array
print(input_array)
#reshaping array to 3 by 5
input_array = input_array.reshape(3,5)
#printing reshaped array
print(input_array.shape)
#replacing max value by 0 in each row
input_array[np.arange(3),np.argmax(input_array, axis=1)]=0
print(input_array)

import numpy as np
#created the 2D array of size 4*3 with 4-byte integer elements. 
input_array = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]], dtype=np.int32)
#print array shape, type and datatype
print("Array Shape :", input_array.shape)
print("Array Type:", type(input_array))
print("Array Datatype:", input_array.dtype)

import numpy as np
input = np.mat("3 -2;1 0")
print("a\n", input)
x, y = np.linalg.eig(input) 
print( "Eigenvalues",x)
print( "Eigenvectors",y)

import numpy as np
l = np.arange(6).reshape(2,3)
print(l)
res =  np.trace(l)
print("Diagonal Sum :",res)

import numpy as np
i = np.array([1, 2, 3, 4, 5, 6])
j = np.reshape(i,(3,2))
print("Reshape 3x2:")
print(j)
k = np.reshape(i,(2,3))
print("Reshape 2x3:")
print(k)

import matplotlib.pyplot as plt
# Data to plot
lang = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
pop = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
# explode 1st slice
explode = (0.1, 0, 0, 0,0,0)  
# Plot
plt.pie(pop, explode=explode, labels=lang, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Popularity of Programming Languages')
plt.axis('equal')
plt.show()