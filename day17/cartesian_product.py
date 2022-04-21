from itertools import product
integer1 = map(int, input().split())
integer2 = map(int, input().split())
A = list(integer1)
B = list(integer2)
cart = list(product(A,B))
print(' '.join(map(str, cart)))