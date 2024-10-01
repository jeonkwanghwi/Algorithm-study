T = int(input())
for test_case in range(T):
    # N은 5~15 , M은 2~N
    n, m = map(int, input().split()) # N*N 배열, m*m크기로 파리채 블로킹
    maps = [] # 영역 1개에 최대 파리는 30마리
    for _ in range(n):
        maps.append(list(map(int, input().split())))
    
    # 파리채 블로킹 시작
    kill_paris = 0 # 죽인 파리 최대 수
    for i in range(n-m+1):
        for j in range(n-m+1):
            comp = 0
            for x in range(m):
                for y in range(m):
                    comp += maps[i+x][j+y]
            kill_paris = max(kill_paris, comp)

    print(f"#{test_case+1}", kill_paris)

