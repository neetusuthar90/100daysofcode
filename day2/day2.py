# x = 100
# y = 30
# z = 50
# if y == 30 and x != 30:
#     print("You are fail")
# if x == 30 or y == 30:
#     print("You achive it")
# if x in [12,100,20,30]:
#     print("Yupp")
# #NOTE: we can also use string 

# if z<x and x<y:
#     print(" false ")
# else:
#     pass

# if x is 100:
#     pass
# elif y is 50:
#     pass
# else:
#     pass

# print(x==y) #print true or false
# #To use not before boolean opertor
# num = None
# if not num:
#     print("yes")

# ### For write the first n natural number
# num = int(input("Enter a number:"))
# N = []
# # for n in range(1,num+1):  both are same 
# for n in range(num):
#     p = n+1
#     N.append(p)
#     n = p
# print(N)

count = 0
N = []
while count<5:
    count = count+1
    print("%d" %count) #  But this will skip 0
while True:
    print(count)
    N.append(count)
    count = count + 1
    if count >20:
        break
print(N)
# Take last digit of N 
for x in N:
    if x%2 != 0:
        print(x)
        continue


    



