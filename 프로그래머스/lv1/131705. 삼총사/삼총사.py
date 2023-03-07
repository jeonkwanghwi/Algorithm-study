from itertools import combinations

def solution(number):
    answer = 0
    
    lst = list(combinations(number, 3))
    
    for i in range(len(lst)):
        if sum(lst[i]) == 0:
            answer += 1
    return answer