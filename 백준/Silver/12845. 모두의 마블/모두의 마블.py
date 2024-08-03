n = int(input())
cards = sorted(list(map(int, input().split())))
print(cards[-1]*(n-1) + sum(cards[:n-1]))