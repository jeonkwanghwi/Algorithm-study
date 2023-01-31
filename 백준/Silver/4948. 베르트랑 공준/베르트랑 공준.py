def isprime(i):
    if i==1:
        return False
    for j in range(2, int(i**0.5)+1):
        if i%j==0:
            return False
    return True


listt = list(range(2,246912))
primes = []
for i in listt:
    if isprime(i):
        primes.append(i)

while True:
    cnt = 0
    n = int(input())
    if n == 0:
        break
    for i in primes:
        if n < i <= n*2:
            cnt+=1
    print(cnt)
