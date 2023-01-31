n = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))

m = costs[0]
result = 0
for i in range(0, n-1):
    if costs[i] < m:
        m = costs[i]
    result += m * roads[i]

print(result)