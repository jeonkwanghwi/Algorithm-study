N=int(input())
score = list(map(int, input().split()))
sum = 0
M = max(score)

for i in range(N):
    score[i] = score[i] / M * 100
    sum = sum + score[i]

print(sum / N)