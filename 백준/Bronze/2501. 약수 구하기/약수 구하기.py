a, b = map(int, input().split())
lst = []
for i in range(1, a+1):
    if a % i == 0:
        lst.append(i)
if len(lst)<b:
    print(0)
else:
    print(lst[b-1])
