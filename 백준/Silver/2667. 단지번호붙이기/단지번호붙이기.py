n = int(input())
graph = []
part_house = 0 # 각 구역별로 집 개수
all_house = [] # 전체 집 개수 list

for i in range(n): # 집 정보 초기화
    graph.append(list(map(int, input())))

# 순서대로 상, 하, 좌, 우로 이동하는 것을 의미
dx = [0, 0, 1, -1] # x축 방향 이동
dy = [1, -1, 0, 0] # y축 방향 이동

def DFS(graph, x, y):
    # 오류가 나는 상황을 정리한 것. 위, 아래로 움직이다가 x, y의 범위 밖으로 나가는 경우를 의미함.
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1: # 1인 집은 탐색 대상임
        global part_house # 구역별 집 개수를 의미함
        part_house += 1
        graph[x][y] = 0 # 탐색 후, 탐색 완료의 의미로 0으로 바꿈
        for i in range(4): # 상하좌우 4개의 방향을 체크함
            nx = x + dx[i] # 기존의 좌표에 상하좌우를 더해줌
            ny = y + dy[i]
            DFS(graph, nx, ny) # 더해준 상하좌우로 다시 탐색
        return True # 모든 탐색이 완료됨
    return False # 탐색이 끝나긴 했는데 0을 만나서 끝남. 즉 1로 둘러싼 경계 밖을 간 것.

# 모든 지점에 대해서 탐색함
for i in range(n):
    for j in range(n):
        if DFS(graph, i, j) == True: # 해당 노드의 상하좌우에 집이 있다면 이라는 뜻임
            DFS(graph, i, j) # 상하좌우에 집 있으니까 방문해야지
            all_house.append(part_house) # DFS 종료 후에 얻은 구역별 집 개수를 넣어줌
            part_house = 0 # 다시 구역별로 집 체크하러 갈 땐 0으로 초기화

all_house.sort()

print(len(all_house))
for i in all_house:
    print(i)