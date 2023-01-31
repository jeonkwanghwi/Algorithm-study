import sys

lst = [0] * 28
for i in range(28):
    lst[i] += int(sys.stdin.readline().strip())

for i in range(1, 31):
    if i not in lst:
        print(i)

       