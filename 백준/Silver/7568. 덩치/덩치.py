import sys

n = int(input())
people = []*n

for i in range(n):
    weight, height = map(int, sys.stdin.readline().strip().split())
    people.append([weight, height, 1])

for i in range(n):
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            people[i][2] += 1
        else:
            continue

for i in range(n):
    print(people[i][2], end=' ')