import numpy as np
prime = [2,3,5,7,11]
even = np.array([x for x in range(2,21,2)])
odd = np.array([x for x in range(1,20,2)])
print(np.array(prime))
print(type(np.array(prime)))
print(np.array([even,odd]))

## Array attribute
print(np.array(prime).dtype) #dataframe
mat = np.array([even,odd])
print(mat.ndim) #dimension of array
print(mat.shape)
print(mat.itemsize)
print(mat.size)

## Print in matrix form
for r in mat:
    for c in r:
        print(c, end = ' ') # End with a space
    print() #print \n only