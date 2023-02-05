import sys
input  = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

# 연속해서 커지거나 작아지거나 - 증가수열 감소수열
dp = [[1] * n for _ in range(2)]

for i in range(1,n):
    if lst[i - 1] <= lst[i]: # 증가
        dp[0][i] = dp[0][i - 1] + 1
    if lst[i - 1] >= lst[i]: # 감소
        dp[1][i] = dp[1][i - 1] + 1
# 증가때랑 감소때를 따로 체크하므로
# 2 2 3 3 에서 2 -> 2 갈때 중복체크하는 일은 없음.

print(max(map(max, dp)))