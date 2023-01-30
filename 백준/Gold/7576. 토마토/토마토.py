# BFS는 queue를 이용하고, 시간 복잡도를 위해서 deque 모듈을 사용해야 한다.

from collections import deque
m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]

queue = deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
answer = 0

# 익은 토마토 위치 찾기
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append([i, j])

# 토마토 익히기
def bfs():
    while queue:
        x, y = queue.popleft() # 익은 토마토 꺼내기

        # 주변 토마토 익히기 (상하좌우)
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y

            # 토마토 익는 조건
            # (1) 익지 않은 토마토인 경우
            # (2) 해당 좌표가 좌표 크기를 넘어가면 안된다.
            if 0 <= nx < n and 0 <= ny < m and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1 # 토마토 익히기 (1로 만들어주기)
                queue.append([nx, ny]) # 익은 토마토 큐에 넣어줌

bfs()

# 토마토 다 익었는지 체크하기
for i in tomato:
    for j in i:
        if j == 0: # 아직 안 익은 토마토가 있다면 -1 출력
            print(-1)
            exit(0)
    # 다 익은 상태면 최댓값이 정답.
    # 왜냐하면 1부터 시작해서 주변을 1씩 키워가며 익혀주는 거라서 최댓값만 찾으면 됨.
    # [9, 8, 7, 6, 5, 4]
    # [8, 7, 6, 5, 4, 3]
    # [7, 6, 5, 4, 3, 2]
    # [6, 5, 4, 3, 2, 1].

    answer = max(answer, max(i))

# 처음 시작을 1로 표현했으니 1을 빼준다.
print(answer - 1)