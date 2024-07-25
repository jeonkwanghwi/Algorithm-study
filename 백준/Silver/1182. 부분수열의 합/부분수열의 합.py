import sys
from itertools import combinations as cb
input = sys.stdin.readline

n, s = map(int, input().split())
lst = list(map(int, input().split()))

# 부분 수열의 합이 s가 되는 개수를 구함
cnt = 0
for i in range(1, n+1):
    tmp = cb(lst, i) # i개 뽑은 조합들이 쭉 들어가있음
    for j in tmp:
        if sum(j) == s:
            cnt += 1
print(cnt)

""" Test Case 주의사항
1. 비어있거나, 하나만 있는 case
2. 첫번째 혹은 맨 마지막 case
3. 크기가 굉장히 큰 case
4. 양수만 있는, 음수만 있는 case
5. overflow가 나는 case
6. 중복 값이 들어가는 case
"""