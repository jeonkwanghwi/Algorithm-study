from collections import Counter
n = int(input())
file = dict()

for i in range(n):
    a, b = input().split('.')
    if b not in file:
        file[b] = 1
    else:
        file[b] += 1

sort_file = sorted(file.items())

for key, value in sort_file:
    print(key.rstrip(), value)