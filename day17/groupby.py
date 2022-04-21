from itertools import groupby

n = input()
p = groupby(n)
l = []
for k, g in p:
    x = len(list(g))
    l.append(tuple([x, int(k)]))

print(' '.join(map(str, l)))
