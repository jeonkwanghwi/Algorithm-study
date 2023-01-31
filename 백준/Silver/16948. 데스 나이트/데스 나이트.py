from collections import deque
import sys
input = sys.stdin.readline

# 이동 경우는 총 8개의 경우가 있고, 각 칸에 해당하는 x축 이동방향과 y축 이동방향을 설정해준다.
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]
flag = 0

def bfs(now_x, now_y, fut_x, fut_y):
    # 초기 설정
    q = deque() # 큐 만들고
    q.append([now_x, now_y]) # 큐에 현재 칸을 넣어줌
    board[now_x][now_y] = 0 # 현재칸의 값을 0으로 설정

    # 나이트 움직이기
    while q:
        a, b = q.popleft() # 큐에서 현재 위치 빼오는데

        # 아직 목적지까지 도달 안했으면 이동하기
        for i in range(6):
            x = a + dx[i]
            y = b + dy[i]

            # 항사 해주는 범위설정과, 가보지 않은 신규 위치인 경우 (값이 0)
            if 0 <= x < n and 0 <= y < n and board[x][y] == -1:
                q.append([x, y])
                board[x][y] = board[a][b] + 1 # 이동하는거는 기존 값 + 1로 이동 횟수 매겨줌



n = int(input()) # 체스판 한변의 길이, 체스판은 n*n 크기
now_x, now_y, fut_x, fut_y = map(int, input().split())
board = [[-1] * n for i in range(n)]
bfs(now_x, now_y, fut_x, fut_y)

print(board[fut_x][fut_y])