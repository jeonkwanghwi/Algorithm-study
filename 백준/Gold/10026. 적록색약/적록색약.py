import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input().rstrip())
lst = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

NoRedGreen_cnt = 0 # 적록색약 아닌 사람이 볼 때 구역의 수
YesRedGreen_cnt = 0 # 적록색약인 사람이 볼 때 구역의 수
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 현재 좌표를 넣어줌
def DFS(x, y):
    visited[x][y] = True # 방문체크
    now_color = lst[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0<= nx <n) and (0<= ny < n):
            if visited[nx][ny] == False:
                # 현재 좌표의 색상과 상하좌우 좌표 색상이 같으면 DFS
                if lst[nx][ny] == now_color:
                    DFS(nx, ny)

# 적록색약 아닌 사람
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            DFS(i,j)
            NoRedGreen_cnt += 1

# R을 G로 바꾸어준다.
for i in range(n):
    for j in range(n):
        if lst[i][j] == 'R':
            lst[i][j] = 'G'

# visited를 초기화
visited = [[False] * n for _ in range(n)]

# 적록색약인 사람
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            DFS(i,j)
            YesRedGreen_cnt += 1


print(NoRedGreen_cnt, YesRedGreen_cnt)