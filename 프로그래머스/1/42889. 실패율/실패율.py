def solution(n, stages):
    stages.sort()
    fail = dict()
    for i in range(1, n+1):
        fail[i] = 0
    ans = []

    for i in range(1, n+1):
        if i not in stages: # 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.
            fail[i] = 0
            continue
        fail[i] = stages.count(i) / (len(stages)-stages.index(i))
        # print(stages.count(i), end=' ')
        # print(len(stages)-stages.index(i))

    # 실패율을 기준으로 내림차순 정렬, 실패율이 같은 경우 스테이지 번호 오름차순 정렬
    sorted_fail = sorted(fail.items(), key=lambda x: (-x[1], x[0]))

    return [keys[0] for keys in sorted_fail]