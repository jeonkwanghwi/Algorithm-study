import sys

rect = [[0]*100 for i in range(100)]

n = int(sys.stdin.readline().strip())

for i in range(n):
    a, b = map(int, sys.stdin.readline().strip().split())
    for x in range(a, a+10):
        for y in range(b, b+10):
            rect[x][y] += 1
cnt = 0
for i in range(100):
    for j in range(100):
        if rect[i][j] != 0:
            cnt += 1

print(cnt)