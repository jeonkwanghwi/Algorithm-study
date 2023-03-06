def solution(n):
    answer = ''
    
    lst = []
    n = str(n)
    for i in range(len(n)):
        lst.append(n[i])
        
    lst.sort(reverse = True)
    
    for i in range(len(lst)):
        answer += lst[i]
    return int(answer)