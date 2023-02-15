n = int(input())
time = list(map(int, input().split()))
time.sort()
cnt = 0
# 정렬 말고 뭐가 더 ??
for i in range(n):
    cnt += sum(time[:i+1])
print(cnt)