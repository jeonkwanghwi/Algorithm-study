import itertools

lst = [int(input()) for _ in range(9)]

ss = list(itertools.combinations(lst, 7))

for i in ss:
    if sum(i)==100:
        for j in sorted(i):
            print(j, end="\n")
        break