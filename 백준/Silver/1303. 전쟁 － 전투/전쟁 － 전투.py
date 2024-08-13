import sys
sys.setrecursionlimit(10**6)

# 가로, 세로 "길이"가 n, m임
n, m = map(int, input().split())  # 가로가 열 개수, 세로가 행 개수라는 것을 헷갈리면 안됨 !!!!!!!!!!!!!!!!!!!!!!!!!!
war = [list(input()) for _ in range(m)] # 여기서도 range(n)이 아니라 m임.

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# white, blue 병사들 총 수
white = 0
blue = 0

# DFS
def find_soldiers(x, y, soldier, color):
    war[x][y] = 0 # 해당 위치는 이제 탐색 안하기 위해 0으로 바꿈

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < m and 0 <= ny < n) and (war[nx][ny] == color): # 상하좌우가 접근범위 내에 있고 and 아군이라면(같은 색이라면)
            soldier = find_soldiers(nx, ny, soldier + 1, color) # 해당 위치로 이동 & 병사 수 1명 늘려줌
    return soldier # dfs 탐색 끝나면 지금껏 탐색한 병사들의 총 수를 리턴


for i in range(m):
    for j in range(n):
        if (war[i][j] == 'W'):
            white += (find_soldiers(i, j, 1, 'W')) ** 2
        elif (war[i][j] == 'B'):
            blue += (find_soldiers(i, j, 1, 'B')) ** 2


print(white, blue)