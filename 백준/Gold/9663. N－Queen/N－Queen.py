n = int(input())
ans = 0
row = [0] * n # 일차원 배열로만 통과되는 ???
# row[i] = j 라고 하면, [i,j]에 놓는다

# 퀸을 해당 위치에 놓을 수 있는지 없는지 검증하는 함수
def is_promising(x):
    # 퀸을 놓지 못하는 경우
    # 1. 같은 열(j값)에 놓인 경우, 즉 row[i] = j 일때 j값이 같은지 확인
    #     같은 행은 확인 X => 왜냐하면 i값 자체가 행을 나타내기 때문에 유일함

    # 2. 대각선 체크
    # 퀸을 위에서부터 채워나가기 때문에 현재 i값의 이전들만 보면 됨. 즉 이전 행들만 본다. 어차피 이후 행들은 아직 안채워져있음
    # 1) 왼쪽 위 대각선
    # 현재 위치가 (3,3)이면 체크할 부분들은 2,2 랑 1,1 랑 0,0
    #
    # 2) 오른쪽 위 대각선
    # 현재 위치가 (3,3)이면 체크할 부분들은 2,4 랑 1,5 랑 0,6


    for i in range(x): # 현재까지 진행한 행(x값)까지만 체크하는 for문
        # or 왼쪽  : 여기가 j값이 같은지 확인하는 부분, 즉 같은 열인지 체크
        # or 오른쪽 : 대각선 체크

        # abs(x-i) : 행끼리 떨어진 거리
        # abs(row[x] - row[i]) : 열끼리 떨어진 거리
        # ㄴ 이 둘이 같을 때가 서로 같은 거리만큼 떨어진 것이므로 대각선을 의미 ex. 행이 1만큼 떨어져있고 열이 1만큼 떨어져있으면
        # 왼쪽위랑 오른쪽위를 고려해줘야함
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return
    else:
        for i in range(n):
            row[x] = i # 파라미터로 넘어온 x는 0이므로 0행부터 놓기 시작, [x,i]에 퀸을 놓는다는 의미 즉 n번째까지 쭉 찍어봄
            if is_promising(x): # 놓을 수 있다면
                n_queens(x + 1) # 그 다음 행을 다룸, 왜냐하면 각 행마다 1개씩이므로 놓을 수 있으면 바로 행 넘어감
n_queens(0)
print(ans)