# 11054
import sys
import operator

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
inc = [1] * n
inc_reverse = [1] * n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and inc[i] <= inc[j]:
            inc[i] = inc[j] + 1

for i in range(n - 1, -1, -1):
    for j in range(i, n):
        if arr[i] > arr[j] and inc_reverse[i] <= inc_reverse[j]:
            inc_reverse[i] = inc_reverse[j] + 1

sys.stdout.write(str(max(map(operator.add, inc, inc_reverse)) - 1))