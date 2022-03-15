from traceback import print_tb
import numpy as np
grade = np.array([[89,98,78],[67,87,98],[89,78,94],[100,90,98]])
print(grade[0,1]) #Elemnet at 01 position
print(grade[0]) #0th row
print(grade[:,0]) #0th coloumn
print(grade[0:3])
print(grade[[1,3]])
print(grade[:,[0,2]])
grade2 = grade.view()
print(grade2) #Same as grade
## But there location are different
print(id(grade))
print(id(grade2))
grade[1] = grade[1]*10 ##We have change 1st row of grade
print(grade,grade2) ## But still grade and grade2 are same