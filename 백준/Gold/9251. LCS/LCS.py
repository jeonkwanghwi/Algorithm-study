import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()

# 같은 게 있기만 하면 된다. 연속적으로 존재하지 않아도 된다. (중요)
# 두 문자열을 비교 -> 이차원 배열

h, w = len(a), len(b)
dp = [[0] * (w+1) for _ in range(h+1)]

# 같은 문자가 있다면 해당 인덱스부터 쭉 뒤로 +1 해준다
# 이전 문자들에 대한 dp는 건드리지 않음 영향이 없으므로
for i in range(1, h+1):
    for j in range(1, w+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j - 1] + 1 # 같으면 이전 dp값 + 1을 지금 dp값에 추가
        else: # 같은 라인 (같은 i값)에 겹치는게 있기만 하면 하나 올려준다는 소리
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
print(dp[-1][-1]) # 누적값이므로 최대값이 여러개일 수 있지만 마지막 값은 반드시 최대값임


