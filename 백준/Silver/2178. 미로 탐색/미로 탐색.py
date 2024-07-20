import sys
from collections import deque
input = sys.stdin.readline

n, m, = map(int, input().split())
maze = [[0] * m for _ in range(n)]
for i in range(n):
    tmp = input().rstrip()
    for j in range(m):
        maze[i][j] = int(tmp[j])

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def BFS(x, y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 내에서 이동하는 상황 & maze 벽이 아닌 경우(값이 0이 아닌 경우)
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1 # 시간을 누적해가듯, 지나간 경로 횟수를 현재 위치에 할당
                queue.append((nx, ny))
    return maze[n-1][m-1]


print(BFS(0,0))