import sys

input = sys.stdin.readline

n, M = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 1, max(trees)

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for i in trees:
        if i > mid: # trees[i] - mid > 0인 경우에만 자를 수 있으므로
            cnt += (i - mid)

    if cnt >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)