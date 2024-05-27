sum1 = 0
max = 0
while(True):
    outper, inper = map(int, input().split(" "))
    if inper == 0:
        break
    sum1 -= outper
    sum1 += inper
    if max < sum1:
        max = sum1

print(max)