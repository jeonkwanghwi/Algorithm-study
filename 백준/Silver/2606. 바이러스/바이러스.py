import sys
input = sys.stdin.readline
sys.setrecursionlimit(5000)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n + 1)
count = 0 # 바이러스에 감염된 컴퓨터 개수

# 연결 리스트로 초기화하는 방법
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v):
    global count
    count += 1
    visited[v] = True
    for i in graph[v]: # i와 연결된 노드중에 방문하지 않았다면 방문
        if not visited[i]:
            dfs(i)


dfs(1)

print(count-1)