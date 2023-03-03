from itertools import combinations

def solution(nums):
    tmplst = list(combinations(nums, 3))
    lst = []
    for i in range(len(tmplst)):
        lst.append(tmplst[i][0] + tmplst[i][1] + tmplst[i][2])
        
    cnt = 0
    for i in lst:
        chk = 0
        for j in range(2, i):
            if i % j == 0:
                chk += 1
        if chk == 0:
            cnt += 1
            
    return cnt