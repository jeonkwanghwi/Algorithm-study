from collections import deque

n, m, v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
visitedDFS = [0] * (n+1)
visitedBFS = [0] * (n+1)

for i in range(m):
    fr, to = map(int, input().split())
    graph[fr][to] = 1
    graph[to][fr] = 1

def DFS(v):
    visitedDFS[v] = 1
    print(v, end=' ')
    for i in range(1, n+1):
        # graph[v][i]가 1인 경우는 정점 v에서 정점 i로 연결된 간선이 있다는 뜻임.
        # 따라서 i를 아직 방문하지 않았다면 DFS(i)로 재귀적으로 탐색함.
        if not visitedDFS[i] and graph[v][i]:
            DFS(i)

def BFS(v):
    queue = deque([v]) # 시작지점을 넣어서 초기화, 큐가 방문 순서를 담아옴
    visitedBFS[v] = 1 # 시작지점 방문처리

    while queue: # 큐가 다 빌때까지
        current = queue.popleft()
        print(current, end = ' ') # 그냥 pop하면 안되고 popleft해야함
        for i in range(n+1):
            if not visitedBFS[i] and graph[current][i]: # 현재의 정점 v랑(current) 연결된 모든 노드를 보고 append해줌. (index 작은것부터 순서대로)
                queue.append(i)
                visitedBFS[i] = 1 # 방문처리
    return queue

# 1이랑 2,3,4 연결
# 2-4 연결
DFS(v) # 1 2 4 3
print()
BFS(v) # 1 2 3 4