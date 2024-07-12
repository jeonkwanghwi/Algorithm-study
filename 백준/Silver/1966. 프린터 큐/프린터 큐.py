from collections import deque

for _ in range(int(input())):
    n, m = map(int, input().split())
    files = deque(list(map(int, input().split())))
    ans = 1

    """ 첫번째 원소가 max보다 작다면 어차피 뒤로 가야해서 m == 0을 체크하지 않음. """

    while len(files) > 0: # 덱 내에 인쇄할 파일이 남아있을 때까지
        if files[0] < max(files): # 첫번째 원소가 max가 아니면 맨 뒤로 보냄(= pop 후 append)
            files.append(files.popleft())

        else: # 첫번째 원소가 max 이상일 때
            if m == 0: # m=0 즉 첫번째 원소를 찾고 있던 거라면 바로 break 종료
                break
            files.popleft() # max 이상이면 바로 pop해도 됨
            ans += 1
        
        if m > 0:
            m -= 1
        else:
            m = len(files) - 1
    print(ans)