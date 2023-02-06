import sys
from collections import Counter

n = int(sys.stdin.readline())
nums = [0] * n

for i in range(n):
    nums[i] = int(sys.stdin.readline().strip())
nums.sort()
nums_freq = Counter(nums).most_common()

avg = round(sum(nums) / len(nums))
mid = nums[n // 2]
bound = nums[-1] - nums[0]
print(avg)
print(mid)
#freq
if len(nums_freq) > 1:
    if nums_freq[0][1] == nums_freq[1][1]:
        print(nums_freq[1][0])
    else:
        print(nums_freq[0][0])
else:
    print(nums_freq[0][0])
print(bound)