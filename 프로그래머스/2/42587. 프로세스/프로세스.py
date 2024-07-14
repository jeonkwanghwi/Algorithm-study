from collections import deque

def solution(priorities, location):
    ans = 0
    priorities = deque(priorities)

    while priorities:  # 안에 있는 값이 다 사라질 때 까지
        if priorities[0] >= max(priorities): # 맨 앞이 최대면 pop
            priorities.popleft()
            ans += 1
            if location == 0:
                break
        else: # 맨 앞이 최대가 아닌 일반적인 경우
            priorities.append(priorities.popleft())
        location -= 1

        if location < 0: # 음수일 때 location 값 보정
            location = len(priorities) - 1

    return ans
