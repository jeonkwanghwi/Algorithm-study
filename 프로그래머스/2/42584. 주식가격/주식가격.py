def solution(prices):
    lst = []
    for i in range(len(prices)):
        ans = 0
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                ans += 1
            else:
                ans += 1
                break
        lst.append(ans)
    return lst