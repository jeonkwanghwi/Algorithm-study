def solution(s):
    dict = {}
    ans = [0] * len(s)

    for i in range(len(s)):
        if s[i] not in dict:
            ans[i] = -1
        else:
            ans[i] = i - dict[s[i]]
        dict[s[i]] = i

    return ans