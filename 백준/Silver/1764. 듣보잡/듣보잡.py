import sys
from collections import Counter

n,m = map(int, sys.stdin.readline().strip().split())
nohear = [0] * n
nosee = [0] * m
#듣도못한
for i in range(n):
    nohear[i] = sys.stdin.readline().strip()
    
#보도못한
for i in range(m):
    nosee[i] = sys.stdin.readline().strip()

counter = Counter(nohear)
cnt = 0
chklist = []
for i in range(m):
    if nosee[i] in counter:
        cnt += 1
        chklist.append(nosee[i])

print(cnt)
chklist.sort()
for i in range(len(chklist)):
    print(chklist[i])