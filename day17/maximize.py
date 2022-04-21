from itertools import product
K,M = map(int,input().split())
dict = []
for i in range(K):
    dict.append(list(map(int, input().split()[1:])))
print(dict)

lst = []
for ele in product(*dict):
    temp = 0
    for i in range(K):
        temp = temp + (ele[i])**2
    S = temp % M
    lst.append(S)
print(max(lst))
