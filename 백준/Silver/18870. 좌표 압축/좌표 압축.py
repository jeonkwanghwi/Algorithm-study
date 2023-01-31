import sys
N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
# 2 4 -10 4 -9
arr2 = list(sorted(set(arr)))
# -10 -9 4 2
dictt = {arr2[i] : i for i in range(len(arr2))}

for i in arr:
    print(dictt[i], end = ' ')