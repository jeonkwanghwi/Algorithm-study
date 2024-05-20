def solution(k, m, score): # k가 최고점, m개의 사과
    score.sort(reverse=True)
    
    sum = 0
    std = len(score)//m
    
    if m>len(score):
        return 0
    
    if m==len(score):
        return min(score)*m
    
    for i in range(1, std+1):
        sum += score[m*i-1] * m

    return sum