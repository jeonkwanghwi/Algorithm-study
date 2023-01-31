n, person = map(int, input().split())
nums= list(map(int, input().split()))
nums.sort()
print(nums[-person])