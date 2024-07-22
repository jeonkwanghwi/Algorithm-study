n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))
visited = [0] * n
temp = []

def backTracking(): # DFS를 이용함
    if len(temp) == m: # 출력조건. m개의 숫자가 쌓일 때까지 백트래킹을 진행함. 다 모이면 출력
        print(*temp)
        return
    prev = 0 # 이전의 값
    for i in range(n): # m개의 숫자가 모이는 과정인데, prev를 통해 중복 출력을 방지함.
        if prev != lst[i] and not visited[i]: # 이전값과 현재값이 다르고, 방문안한 경우
            visited[i] = True # 방문처리
            temp.append(lst[i]) # 현재값 temp에 넣음 (m개까지 모을거임)
            prev = lst[i] # 현재값은 이제 prev값으로 바뀜
            backTracking()

            # 재귀 호출이 끝나면 방문 여부를 해제 & 마지막으로 추가한 요소를 제거
            visited[i] = False
            temp.pop()

backTracking()