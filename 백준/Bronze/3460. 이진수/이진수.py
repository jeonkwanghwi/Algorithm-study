a = int(input())
lst = []
for i in range(a):
    lst.append(int(input()))

for i in range(len(lst)):
    n = lst[i]
    newn = bin(n)  # 0b1101
    newn = newn[2:]
    newn = newn[::-1]

    for i in range(len(newn)):
        if int(newn[i]) == 1:
            print(i, end=" ")
    print()
