def check(s):
    # ( { [ 다 체크해야함.
    stack = []
    for c in s:
        if c == "(" or c == "{" or c == "[":
            stack.append(c) # 여는 괄호는 다 넣어줌
        else: # 닫는 괄호 체크하기
            if len(stack) == 0: # 처음 오는 닫는괄호일 땐 바로 컷
                return False

            # 여기부턴 여는 괄호 있는 경우임
            last = stack.pop()
            # 짝이 맞으면 이어서 진행
            if (c == ")" and last == "(") or (c == "}" and last == "{") or (c == "]" and last == "["):
                continue
            # 짝 안맞으면 무조건 False
            else:
                return False
    return len(stack) == 0


# 리스트 회전시키기 (중요 !!!!!!!!!!!!) - 리스트는 rotate 없음.
# 회전 쓰려면 deque 써야하는데, 이거 짧고 좋아서 기억하기
def right_rotate(tmp_list, n): # 오른쪽으로 n만큼 회전하기
    # 오른쪽 회전
    return tmp_list[-n:] + tmp_list[:-n]

    # 왼쪽 회전은 tmp[n:] + tmp[:n]

def solution(s):
    ans = 0
    s = list(s)
    for i in range(len(s)):
        if check(s): # 괄호 짝 다 맞으면
            ans += 1
        s = right_rotate(s, 1) # 왼쪽 오른쪽 상관없음
    return ans

