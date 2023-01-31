n = input()

nums = []
for i in range(len(n)):
    nums.append(int(n[-i]))
nums.sort(reverse=True)

for i in range(len(nums)):
    print(nums[i], end='')