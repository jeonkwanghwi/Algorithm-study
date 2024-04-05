n = int(input())
lst = list(map(int, input().split()))
b, c = map(int, input().split())
cnt = 0

for i in range(len(lst)):
    lst[i] -= b
    cnt += 1

    if lst[i] < 0:
        continue

    if lst[i] % c == 0:
        cnt += (lst[i]//c)
    else:
        cnt = cnt + (lst[i]//c) + 1

print(cnt)