duck = input()
visited = [False] * len(duck)
cnt = 0

# 녹음이 잘못 된 경우 - quack 가 온전히 녹음되지 않아서 텍스트가 5의 배수가 아닌 경우
if len(duck) % 5 != 0:
    print(-1)
    exit()

# 한바퀴 돌동안 quack이 몇번 반복되는가??
# 최소 오리를 구해야돼서, quack을 다 찾는 동안 전체를 몇바퀴 돌았는지 체크
def sol(start):
    global cnt
    prev = None
    q_cnt = 0 # 시작
    k_cnt = 0 # 끝

    for i in range(start, len(duck)):

        # q
        if not visited[i] and duck[i] == 'q' and q_cnt == 0:
            visited[i] = True
            prev = duck[i] # 이 다음 u는 q가 이전 문자일테니까 현재 문자를 prev에 저장
            q_cnt += 1
            continue
        elif not visited[i] and duck[i] == 'q' and prev == 'k': # k 다음 바로 q로 오리가 연속으로 소리를 낸 경우
            visited[i] = True
            prev = duck[i]
            continue

        # u, a, c는 q와 k 사이에 있어서 끝나는 경우(k)와 상관 없어서 그냥 앞에 문자만 확인하고 prev 갱신
        # u
        if not visited[i] and duck[i] == 'u' and prev == 'q':
            visited[i] = True
            prev = duck[i]
            continue
        # a
        if not visited[i] and duck[i] == 'a' and prev == 'u':
            visited[i] = True
            prev = duck[i]
            continue
        # c
        if not visited[i] and duck[i] == 'c' and prev == 'a':
            visited[i] = True
            prev = duck[i]
            continue

        # k
        # k에서 오리를 완성
        if not visited[i] and duck[i] == 'k' and prev == 'c' and k_cnt == 0:
            visited[i] = True
            prev = duck[i]
            cnt += 1 # 오리 한마리 증가
            k_cnt += 1
            continue

        # 아직 한바퀴 다 안돌았는데 오리가 이미 완성되어있는 경우. k_cnt가 1이상이라면 이미 앞에서 오리가 만들어져있는거고
        # 지금 오리문자열의 중간 어딘가에 있는거임. 그래서 오리 울음소리가 하나 더 있다고 해도
        # 앞에 오리가 이미 만들어져있기 때문에 그 오리 울음소리로 퉁침. (오리 최소를 구하는 것이므로.)
        # 그래서 여기서는 방문체크랑 prev 갱신만 해주고 오리 개수인 cnt를 늘려주지는 않음.
        elif not visited[i] and duck[i] == 'k' and prev == 'c' and k_cnt > 0:
            visited[i] = True
            prev = duck[i]
            continue


for i in range(len(duck)):
    if duck[i] == 'q' and not visited[i]: # 맨 처음은 q이고, 방문하지 않았어야함.
        # 한바퀴 돌면 오리 몇마리 만들어지고, 그 다음엔 q이면서 아직 체크 안한 부분을 보는 것.
        # 즉, 맨 처음에 끝까지 돌면서 오리 갱신하고, 그 다음에 두번째부터 다시 찾기 시작하는데
        # quqacukqauackck라고 하면 두번째인 u는 방문했을테니 스킵하고 다시 q를 찾는것.
        # 거기서부터 다시 오리찾기 시작 => sol(i)
        sol(i)

# 모든 문자열을 방문하지 않았거나 오리가 0마리면 녹음이 잘못된 것.
if False in visited or cnt == 0:
    print(-1)
else:
    print(cnt)