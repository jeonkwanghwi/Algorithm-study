n = int(input())
lst = [float(input()) for _ in range(n)]

for i in range(1, n):
    lst[i] = max(lst[i - 1] * lst[i],   lst[i]) # 이전것 * 지금 vs 지금

print("{:.3f}".format(max(lst)))