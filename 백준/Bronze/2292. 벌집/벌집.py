n = int(input())
chknum = 1
i=0
if n == 1:
    print(1)
    exit()

while not(n <= chknum):
    chknum = chknum + 6*i
    i += 1
    
print(i)