import sys


n = int(sys.stdin.readline())
temp = dict() # 딕셔너리 형

# 반복문을 통해 출입 기록울 확인한다.
for _ in range(n):
    a, b = map(str, sys.stdin.readline().split())

    # 출입을 했으면 딕셔너리로 받는다.
    if b == "enter":
        temp[a] = b
    # 퇴근을 했으면 삭제해준다.
    else:
        del temp[a]

# 사전 순의 역순으로 정렬한다.
temp = sorted(temp.keys(), reverse=True)

for i in temp:
    print(i)