n, purpose = map(int, input().split())
lan_cm = [0] * n
for i in range(n):
    lan_cm[i] = int(input())

start, end = 1, max(lan_cm)

# binary search가 target을 설정해놓고 존재여부를 찾는 느낌으로만 많이 썼는데
# 이 문제에서는 target이 미정인 상태에서 이분탐색을 쓴 것이 핵심이었다고 생각.
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(n):
        cnt += (lan_cm[i] // mid)

    # 만약 잘라서 만들어진 랜선의 개수가 목표보다 많으면 길이가 짧은 거로 여러번 자른 것이므로
    # 랜선의 길이가 길어져야함. 그래서 mid의 오른쪽을 탐색하도록 설정
    if cnt >= purpose:
        start = mid + 1
    # 자른 개수 cnt가 목표 개수보다 적으면 랜선의 길이를 너무 길게 해서 자른 것이므로
    # mid의 왼쪽을 찾아서 랜선 길이를 줄여줌
    else:
        end = mid - 1
print(end)