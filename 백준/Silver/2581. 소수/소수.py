m = int(input())
n = int(input())
cnt = 0
primenums = []

for chk in range(m, n+1): # m 이상 n 이하 자연수 중에 소수찾기
    notprime = 0
    if chk == 1:
        continue
    else:
        for j in range(2, chk):
            if chk % j == 0:
                notprime = 1

    if notprime == 0:
        cnt += 1
        primenums.append(chk)

if cnt == 0:
    print(-1)
else:
    print(sum(primenums))
    print(min(primenums))