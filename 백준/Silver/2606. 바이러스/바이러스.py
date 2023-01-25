n = int(input())
v = int(input())

# 경로를 저장하기 위한 2차원 리스트
graph = [[] * n for _ in range(n + 1)]

for _ in range(v):
    a, b = map(int, input().split())
    graph[a].append(b) # index와 값으로 서로를 연결해줌
    graph[b].append(a) # 즉, 해당 인덱스에 값이 있으면 연결되어 있는 것.

cnt = 0
visited = [0] * (n + 1) # 모두 0으로 초기화, 0은 방문안한거고 1은 방문한것

def dfs(start):
    global cnt
    visited[start] = 1 # 방문 체크
    for i in graph[start]:
        if visited[i] == 0: # 만약 방문 안했다면
            dfs(i)
            cnt += 1 # dfs 빠져나오고서, 방문한 노드 개수 하나 증가

dfs(1) # 1번부터 시작
print(cnt)