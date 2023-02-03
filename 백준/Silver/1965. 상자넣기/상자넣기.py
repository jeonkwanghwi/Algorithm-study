import sys
input = sys.stdin.readline

n = int(input())
box = list(map(int, input().split()))
lis = 0

result = [1] * n

# 증가부분, 감소부분은 11053의 처음 LIS 문제랑 코드가 완전 동일

for i in range(n):
    for j in range(i):
        if box[i] > box[j]:
            result[i] = max(result[i], result[j] + 1)

print(max(result))