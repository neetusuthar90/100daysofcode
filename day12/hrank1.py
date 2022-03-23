x = int(input())
y = int(input())
z = int(input())
n = int(input())
"""  
[i,j,k] = [0,0,1],[1,2,1] etc
"""

# grid = [] 
# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#              grid.append([i,j,k])
# print(grid)
grid = [(i,j,k) for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]
print(grid)
