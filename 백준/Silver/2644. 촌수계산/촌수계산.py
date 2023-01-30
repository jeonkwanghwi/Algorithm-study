
# 트리 탐색하기 문제
def dfs(v, num):
  num += 1
  visited[v] = True

  # 찾아야 하는 사람의 번호를 방문했을 때
  if v == b:
    answer.append(num)

  for i in family[v]:
    if not visited[i]: # 노드 방문
      dfs(i, num)

################################################################
n = int(input()) # 전체 사람의 수
a, b = map(int, input().split()) # 촌수를 계산해야하는 두 사람의 번호 // 다시말해서 시작노드와 도착노드
m = int(input()) # 부모 자식들 간의 관계의 개수
family = [[] for _ in range(n + 1)] # 부모 - 자식 2차원 배열
visited = [False] * (n + 1)
answer = []

for _ in range(m):
  x, y = map(int, input().split()) # 부모 자식간의 관계를 나타내는 두 번호
  family[x].append(y)
  family[y].append(x)
################################################################


dfs(a, 0)

if len(answer) == 0: # 친척 관계 아닐때
  print(-1)
else:
  print(answer[0] - 1)