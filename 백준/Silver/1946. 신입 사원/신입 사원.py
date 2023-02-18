import sys
input = sys.stdin.readline

T = int(input())
# 점수가 아니라 순위가 입력됨

for _ in range(T):
    N = int(input())
    apply = [list(map(int, input().split())) for _ in range(N)]
    ###########################
    apply.sort() # 서류심사에 대해서만 정렬됨.
    
    # 서류점수와 면접점수 둘 다 동시에 정렬은 불가능하므로
    # 일단 하나에 대해서만 정렬을 쭉 해두고
    # 그 상태에서 면접 점수들만 비교.
    
    top = 0 # 비교시 기준이 되는 사람의 인덱스 번호. top = 0이면 처음 시작하는 사람을 의미
    result = 1 # 첫번째 사람은 서류가 1등이니까 무조건 채용, 그래서 결과를 1로 두고 시작

    # 서류성적에 대해서는 정렬이 되어 있으므로
    # 뒤에 있는 사람이 합격하려면 반드시 앞에 사람보다 면접 등수가 높아야함.
    # top(현재 사람의 면접 등수)보다 높은 등수가 있다면 합격처리.
    for i in range(1, len(apply)):
        if apply[i][1] < apply[top][1]:
            top = i # 높은 사람이 있다면 top을 교체
            result += 1
            
    # EX
    # 면접 등수 순서가 4 3 5 2 1 라고 한다면
    # 4 < 3 이므로 2번째 사람이 합격하고, top을 인덱스 1로 교체
    # 3 > 5 이므로 불합격, top은 그대로 1로 유지
    # 3 < 2 이므로 합격, top을 인덱스 3으로 교체.
    # 2 < 1 이므로 합격, top을 인덱스 1로 교체
    

    print(result)