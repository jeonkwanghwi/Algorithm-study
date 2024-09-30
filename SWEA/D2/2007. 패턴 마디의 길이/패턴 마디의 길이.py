T = int(input())

for t in range(T):
    lst = input() # 문자열 길이는 30 고정

    for i in range(1, 11): # 1부터 10까지 마디 잘라봄 (마디 최대 길이가 10)
        pattern = lst[:i] # 이 패턴이 "연속으로" 반복되느냐? 를 봐야함.
        if lst.startswith(pattern * (30 // i)): # startswith : 문자열이 특정 패턴으로 시작하는가 ?
            print(f"#{t + 1} {i}")
            break

        """ 아래 코드 안되는 이유 : 문자열 lst가 꼭 패턴만큼 주어지는게 아님.
        KoreaKo 처럼 패턴은 5글자인데 lst가 7글자 주어질 수 있음.
        그래서 패턴을 n배 했을 때 안될수도 있는 것."""
        # if lst == pattern * (30 // i): # 즉, 패턴 연속으로 이어붙였을 때 원래의 문자열이 되느냐 ?
        #     break v