from collections import deque

n, k = map(int, input().split())
maxSize = 100000
visited = [0] * (maxSize + 1)  # 10만 1

def bfs(start):
    queue = deque()
    queue.append(start)

    while queue:
        current = queue.popleft()
        if current == k: # 탈출 조건
            return visited[k] # value가 결국 time값
        
        for next in (current+1, current-1, current * 2): # 이동할 수 있는 경우는 이 3가지뿐
            if 0 <= next <= maxSize and not visited[next]:
                visited[next] = visited[current] + 1
                queue.append(next)


print(bfs(n))