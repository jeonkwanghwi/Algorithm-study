# 15650 N과 M (2)
import itertools

n, r = map(int, input().split())
a = []
for i in range(1, n+1):
    a.append(str(i))
nCr = itertools.combinations(a, r)
nCr = list(nCr)
for i in range(len(nCr)):
    for j in range(r):
        print(nCr[i][j], end=' ')
    print()