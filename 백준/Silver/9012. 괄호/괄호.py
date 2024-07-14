from collections import deque
n = int(input())

for _ in range(n):
    dq = deque(input())
    compare = 0

    if dq.count("(") != dq.count(")"): # 괄호의 개수 자체가 다르면 비교 X
        print("NO")
        continue

    """
    (은 )보다 항상 많거나 같아야 한다는 것을 이용
    개수를 체크하면서 compare 값을 늘려서 음수가 된다면 ())와 같은 상황이므로 NO
    """
    for i in dq:
        if i == "(":
            compare += 1
        elif i == ")":
            compare -= 1
        if compare < 0:
            print("NO")
            break
    if compare == 0:
        print("YES")