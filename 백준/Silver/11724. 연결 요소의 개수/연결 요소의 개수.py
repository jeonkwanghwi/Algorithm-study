import sys
input = sys.stdin.readline
sys.setrecursionlimit(5000)

n, m = map(int, input().split()) # 정점개수 n , 간선개수 m
graph = [[] for _ in range(n+1)]
visited = [False] * (n + 1)
count = 0 # 연결 요소 개수

# 연결 리스트로 초기화하는 방법
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

for i in range(1, n+1):
    if not visited[i]:
        count += 1
        dfs(i)

print(count)