# 목표 : 0(안전영역) 개수의 최댓값은 ?
# 바이러스들은 상하좌우로만 이동 가능.
# 2에서부터 시작하여 주변의 0들을 2로 만들어주면 된다.

# 어디 벽을 세워야 최대인가?? =? 모른다. 따라서 모든 경우를 다 따져본다. --> 벽을 세우고 BFS 수행 후 벽을 지우고
# 그 다음 칸에 벽을 세우고 BFS하고 지우고 .... == 백트래킹 방식 // 벽을 반드시 3개 세워야 하기 때문에
# 백트래킹으로 것. 세워보고 값 저장하고, 이전 값이랑 비교해서 버리고 .... 반복 ...
# 즉, 벽을 3개 세우고 바이러스가 퍼진 상태에서 0의 개수를 세면 된다.


from collections import deque
import copy

# 바이러스가 퍼지는 것이 BFS
# 바이러스 퍼뜨린 후에 안전영역 체크하기
def bfs():
    queue = deque()
    # 백트레킹을 해야되니까 원래 그래프를 오염시키지 않으려고 tmp 생성 (?)
    tmp_graph = copy.deepcopy(graph)

    # 큐에 바이러스(2인곳)를 모두 넣어줌.
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                queue.append((i, j)) # 해당 영역의 좌표들을 append

    # 바이러스가 어디로 퍼져나갈 수 있는지 체크
    while queue:
        x, y = queue.popleft()

        # 상하좌우를 체크해줌
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 예외상황 처리, 좌표가 음수거나 최대범위를 넘어가면 continue (?)
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if tmp_graph[nx][ny] == 0: # 안전영역일 때
                tmp_graph[nx][ny] = 2 # 오염시켜버림
                queue.append((nx, ny)) #오염시키고 바이러스 큐에 넣어줌
    # 오염 완료 #

    global answer # 안전영역의 개수
    cnt = 0

    # 안전영역 0 개수를 세어 넣어줌
    for i in range(n):
        cnt += tmp_graph[i].count(0) # 각 행별로 0의 개수 세기

    # 안전영역 최대 개수만 있으면 됨
    answer = max(answer, cnt)


# 벽 세우기
def makeWall(cnt):

    # 벽을 3개까지만 세울 수 있어서, 벽 3개 세웠으면(0,1,2) 그만 하고 이제 BFS(바이러스 퍼뜨리기) 실행하고 종료.
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0: # 빈 공간이라면 벽 세우기 가능
                graph[i][j] = 1 # 벽을 세우고
                makeWall(cnt+1) # 다시 두번째 벽 세우러 간다
                graph[i][j] = 0 # 다시 벽을 허무는 과정 (백트래킹)


n, m = map(int, input().split())
graph = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    graph.append(list(map(int, input().split())))
answer = 0
makeWall(0)

print(answer)