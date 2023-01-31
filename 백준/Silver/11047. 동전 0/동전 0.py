import sys

n, money, = map(int, input().split())
money_list = [0] * n
for i in range(1, n+1):
    money_list[n-i] = int(sys.stdin.readline().strip())
cnt = 0
i = 0
while money != 0:
    if money >= money_list[i]:
        cnt += money // money_list[i]
        money = money % money_list[i]
        i += 1
    else:
        i += 1

print(cnt)