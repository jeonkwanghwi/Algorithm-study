n, s, m = map(int, input().split())
v = list(map(int, input().split()))

def max_volume(n, s, m):
    # dp[i][j]는 i번째 곡을 연주할 때 볼륨이 j인 상태를 나타낸다.
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # 시작 볼륨 설정 : dp[0][S] = True
    dp[0][s] = True

    for i in range(n):
        for j in range(m + 1):
            if dp[i][j]: # 현재 i번째 곡을 연주할 때 볼륨이 j인 상태인지 확인
                if j + v[i] <= m: # 볼륨을 증가시키는 경우 (단, 최대 볼륨 M을 넘지 않아야 함)
                    dp[i + 1][j + v[i]] = True
                if j - v[i] >= 0: # 볼륨을 감소시키는 경우 (단, 최소 볼륨 0보다 작지 않아야 함)
                    dp[i + 1][j - v[i]] = True

    # 마지막 곡의 가능한 볼륨 중 최대값 찾기
    for vol in range(m, -1, -1):
        if dp[n][vol]:
            return vol

    # 가능한 볼륨이 없으면 -1 반환
    return -1


print(max_volume(n, s, m))
