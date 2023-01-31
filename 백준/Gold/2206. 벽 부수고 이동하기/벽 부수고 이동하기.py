from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
########################### 입력받기

# 벽을 한개까지는 부수고 갈 수 있음.
# 이동은 상하좌우만 가능.
# 최단경로 이동이기 때문에 BFS 사용
# Q. 혹시  그럼  DFS 사용하는 경우는 언제인가요??

# 3차원 행렬을 통해 벽의 파괴를 파악함. visited[x][y][0]은 벽 파괴 가능. [x][y][1]은 불가능.
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1


# 상하좌우 이동만 가능
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y, z):
    queue = deque()
    queue.append((x, y, z))

    while queue:
        a, b, c = queue.popleft()

        # 탈출조건, 맨 끝에 도달시
        if a == n - 1 and b == m - 1:
            return visited[a][b][c]


        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 이동은 벽으로, 혹은 벽이 아닌곳으로 이동할 수 있는데
            # 벽인 곳으로 갈 때에는 반드시 벽 부술 기회를 안썼을 때만 갈 수 있고
            # 벽이 아닌 곳을 갈 때에는 아직 방문을 안했을 때에만 갈 수 있다.

            # 다음칸이 벽(1)이고, c=0일때 즉 아직 벽을 안부셨을 경우
            if graph[nx][ny] == 1 and c == 0 :
                visited[nx][ny][1] = visited[a][b][0] + 1
                queue.append((nx, ny, 1))
            # 다음칸이 이동가능한 칸(0)이고 아직 방문 안했다면
            elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = visited[a][b][c] + 1
                queue.append((nx, ny, c))
    return -1

print(bfs(0, 0, 0))