n = int(input())

def onetwoThree(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 4
    else:
        return onetwoThree(n-1) + onetwoThree(n-2) + onetwoThree(n-3)

for i in range(n):
    a = int(input())
    print(onetwoThree(a))