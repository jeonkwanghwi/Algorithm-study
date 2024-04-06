from itertools import combinations

person, chicken = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(person)]
cnt = 0

for a,b,c in combinations(range(chicken), 3):
    tmp = 0
    for i in range(person):
        tmp += max(lst[i][a], lst[i][b], lst[i][c])
    cnt = max(tmp, cnt)

print(cnt)