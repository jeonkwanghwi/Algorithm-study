import sys
input = sys.stdin.readline
sys.setrecursionlimit(5000)

earthworm = 0
# 순서대로 상, 하, 좌, 우로 이동하는 것을 의미
dx = [0, 0, 1, -1] # x축 방향 이동
dy = [1, -1, 0, 0] # y축 방향 이동

def DFS(x, y):
    # 오류가 나는 상황을 정리한 것. 위, 아래로 움직이다가 x, y의 범위 밖으로 나가는 경우를 의미함.
    if x < 0 or x >= width or y < 0 or y >= height:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        for i in range(4): # 상하좌우 4개의 방향을 체크함
            nx = x + dx[i] # 기존의 좌표에 상하좌우를 더해줌
            ny = y + dy[i]
            DFS(nx, ny) # 더해준 상하좌우로 다시 탐색
        return True # 모든 탐색이 완료됨
    return False # 탐색이 끝나긴 했는데 0을 만나서 끝남. 즉 1로 둘러싼 경계 밖을 간 것.

for _ in range(int(input())):
    width, height, cabbages = map(int, input().split()) # 배추밭 가로, 배추밭 세로, 배추개수
    graph = [[0] * (height) for _ in range(width)]  # 배추밭 초기화
    visited = [[0] * (height) for _ in range(width)]
    earthworm = 0  # 지렁이

    # 배추가 심어져 있는 곳 초기화
    for _ in range(cabbages):
        u, v = map(int, input().split())
        graph[u][v] = 1

    for x in range(width):
        for y in range(height):
            if graph[x][y] == 1:
                DFS(x, y)
                earthworm += 1
    print(earthworm)