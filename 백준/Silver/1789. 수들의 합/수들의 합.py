
n= int(input())
i = 0
cnt = 0

while True:
    if n < i:
        print(i-1)
        break
    else:
        n = n-i
        i += 1

