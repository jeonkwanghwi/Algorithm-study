n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

visited = [[0] * n for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

total_area = 0 # 총 단지 수
each_house = 0 # 단지별 집 개수
tmp = []

def DFS(x, y):
    global each_house
    if (0<=x<n and 0<=y<n) is False:
        return

    if not visited[x][y] and graph[x][y]:
        visited[x][y] = 1
        each_house += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            DFS(nx, ny)
        return True
    return True

for i in range(n):
    for j in range(n):
        if graph[i][j] and not visited[i][j]:
            DFS(i,j)
            total_area += 1
            tmp.append(each_house)
            each_house = 0

tmp.sort()
print(total_area)
for i in range(total_area):
    print(tmp[i])