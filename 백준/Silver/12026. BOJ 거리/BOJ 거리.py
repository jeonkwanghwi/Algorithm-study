n = int(input())
boj = input()
dp = [1000001]*n
dp[0] = 0

for i in range(n):
    for j in range(i+1, n):

        idx = j-i

        if boj[i]=="B" and boj[j]=="O":
            dp[j] = min(dp[j], dp[i] + idx**2 )

        if boj[i]=="O" and boj[j]=="J":
            dp[j] = min(dp[j], dp[i] + idx**2 )

        if boj[i]=="J" and boj[j]=="B":
            dp[j] = min(dp[j], dp[i] + idx**2 )


if dp[-1] == 1000001:
    print(-1)
else:
    print(dp[-1])