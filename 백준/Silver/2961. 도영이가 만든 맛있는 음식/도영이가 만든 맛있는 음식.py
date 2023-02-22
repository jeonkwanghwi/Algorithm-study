import sys, itertools
from itertools import combinations
input = sys.stdin.readline

n = int(input())
sour = [] # 신맛, 곱
bitter = [] # 쓴맛, 합

for _ in range(n):
    a, b = map(int, input().split())
    sour.append(a)
    bitter.append(b)

diff = 1000000000 # 차이는 맛의 최댓값으로 초기설정

for i in range(1, n+1): # 재료를 i개 뽑을 때
    lst = list(combinations(list(range(n)), i)) # 가능한 경우를 담은 리스트

    for food in lst: # 경우 하나씩 탐색
        s = 1
        b = 0

        for j in range(i): # 맛 계산
            s *= sour[food[j]]
            b += bitter[food[j]]
            
        diff = min(diff, abs(s-b))

print(diff)