import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
sensor = sorted(list(map(int, input().split())))
# 집중국의 수신 가능 영역의 길이의 합의 최솟값은 ?

# 집중국수 k가 센서수 n보다 같거나 크다면
# 집중국을 센서 위치에 설치하면 되므로 답은 0
if k >= n:
    print(0)
    sys.exit()

# 센서들간의 거리를 계산해서 담는다
# ex. 1 3 6 6 7 9 이라면 거리는 2 3 0 1 2
distance = []
for i in range(1, n):
    distance.append(sensor[i] - sensor[i - 1])

# 센서들을 집중국 수만큼 나누어야 한다. 즉 k개의 구간으로 나누어야 해서
# 거리를 내림차순 하고 k-1번 만큼 반복을 하며 값이 가장 큰 원소부터 차례로 제거한다.

# 즉, 1-3 / 3-6 / 6-6 / 6-7 / 7-9 가 서로 연결되어 있는건데
# 이중에서 가장 큰 차이를 가진 부분부터 지운다는 소리.
# 그렇게 남은 거리들만 합쳐줌
distance.sort(reverse=True)
for _ in range(k-1):
    distance.pop(0)

print(sum(distance))