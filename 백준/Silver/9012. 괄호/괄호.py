from collections import deque
n = int(input())

for _ in range(n):
    dq = deque(input())
    compare = 0

    if dq.count("(") != dq.count(")"): # 개수 자체가 다르면 비교 X
        print("NO")
        continue

    for i in dq:
        if i == "(":
            compare += 1
        elif i == ")":
            compare -= 1
        if compare < 0:
            print("NO")
            break
    if compare >= 0:
        print("YES")