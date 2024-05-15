def solution(s):
    lst = []
    dict = {}
    ans = [0] * len(s)

    for i in range(len(s)):
        if s[i] not in dict:
            dict[s[i]] = i
            ans[i] = -1
        else:
            ans[i] = i - dict[s[i]]
            dict[s[i]] = i # 현재 인덱스로 업데이트

    return ans