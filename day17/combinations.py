from itertools import combinations

name, r = input().split()
for i in range(int(r)):
    name1 = ''.join(sorted(name))
    per = list(combinations(name1,i+1))
    res = [''.join(tups) for tups in per]
    print('\n'.join(map(str, res)))
