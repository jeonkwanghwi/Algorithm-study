import sys
import heapq

input = sys.stdin.readline
n = int(input())
room = []
heap = []

# heapq로 list배열을 힙처럼 사용할 수 있게 해준다.
# heapq.heappush , heapq.heappop
for i in range(n):
    a, b = map(int, input().split())
    room.append([a, b])
room.sort(key=lambda x: x[0])


heapq.heappush(heap, room[0][1]) # 회의실 때처럼 기준이 되는 첫 강의시간을(끝나는 시간) 넣어줌
for i in range(1, n):
    if heap[0] > room[i][0]: # 끝나는 시간이 시작 시간보다 크다면 다음 수업을 들을 수 있음.
        heapq.heappush(heap, room[i][1])
    else:
        heapq.heappop(heap) # 끝나는 시간 < 시작시간이라면 볼 필요 없으므로 pop
        heapq.heappush(heap, room[i][1]) # 그리고 그 다음 값(그 다음 끝나는 시간)을 heap에 넣어줌

print(len(heap))