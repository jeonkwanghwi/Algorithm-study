n = int(input())
boj = input()
dp = [1000001]*n
dp[0] = 0

for i in range(n):
    for j in range(i+1, n):
        if (boj[i]=="B" and boj[j]=="O") or (boj[i]=="O" and boj[j]=="J") or (boj[i]=="J" and boj[j]=="B"):
            dp[j] = min(dp[j], dp[i] + (j-i)**2 ) # j-i는 인덱스끼리 떨어진 거리를 의미함
if dp[-1] == 1000001:
    print(-1)
else:
    print(dp[-1])