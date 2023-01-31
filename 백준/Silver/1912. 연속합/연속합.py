


import sys

n = int(input())
nums = list(map(int, sys.stdin.readline().strip().split()))
# 핵심 - 내가 너랑 힘을 합치는게 이득이냐 아니냐를 따지는것
for i in range(1, n):
    nums[i] = max(nums[i], nums[i-1] + nums[i])
print(max(nums))