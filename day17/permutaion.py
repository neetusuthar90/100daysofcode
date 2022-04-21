from itertools import permutations

name, r = input().split()
per = list(permutations(name,int(r)))
res = [''.join(tups) for tups in per]
res.sort()
print('\n'.join(map(str, res)))