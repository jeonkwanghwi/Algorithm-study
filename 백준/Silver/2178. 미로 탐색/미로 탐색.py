from collections import deque

n, m, = map(int, input().split())
graph = []
visited = [[0] * m for _ in range(n)]
for _ in range(n):
    graph.append(list(input()))

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def BFS(a, b):
    queue = deque() # 덱 초기화
    queue.append((a,b)) # 초기값 append
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and int(graph[nx][ny])==1: # 범위 내고, 이동할 수 있는 위치라면 (그래프값이 1)
                graph[nx][ny] = int(graph[x][y]) + 1
                queue.append((nx, ny))
    return graph[n-1][m-1] # 누적하면서 끝을 도달하니깐 맨 마지막 위치의 값이 정답

print(BFS(0,0))