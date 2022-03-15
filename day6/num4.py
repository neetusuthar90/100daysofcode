import numpy as np
grade = np.array([[89,98,78],[67,87,98],[89,78,94]])
print(grade.mean())
print(grade.max())
# Row/column wise
"""No need to use loops"""
print(grade.max(axis=1)) #Each rom max
print(grade.min(axis=0)) #Ecah coloumn maximum
print(grade.std())
rd = np.random.randint(60,101,12).reshape(3,4)
print(rd.mean(axis=0))
print(rd.mean(axis=1))
pow = np.power(grade,3)
print(pow)