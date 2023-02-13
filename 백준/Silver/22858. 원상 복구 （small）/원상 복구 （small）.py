import sys
input = sys.stdin.readline

N, K = map(int, input().split())
Pi = list(map(int, input().split()))
Di = list(map(int, input().split()))

for _ in range(K):
    tmp = [0]*N
    for i in range(N):
        tmp[Di[i] - 1] = Pi[i]
    Pi = tmp.copy()

for i in range(len(Pi)):
    print(Pi[i], end=' ')
