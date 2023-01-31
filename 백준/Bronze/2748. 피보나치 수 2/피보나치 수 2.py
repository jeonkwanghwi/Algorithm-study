n = int(input())
fibo = [1] * 91
fibo[1] = 1
fibo[2] = 1
for i in range(3, n+1):
    fibo[i] = fibo[i-2] + fibo[i-1]
print(fibo[n])