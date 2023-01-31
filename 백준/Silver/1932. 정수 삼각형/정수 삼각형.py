n = int(input())
pre = [0]

for i in range(n):
    now = list((map(int, input().split())))

    # if i == 0: # 초기화 작업 ...??
    #     pre[0] = now[0]
    #     continue
    for j in range(i+1):
        if j == 0:
            now[0] += pre[0]
        elif j == i:
            now[i] += pre[i-1]
        else:
            now[j] += max(pre[j-1], pre[j])
    pre = now.copy()

print(max(now))