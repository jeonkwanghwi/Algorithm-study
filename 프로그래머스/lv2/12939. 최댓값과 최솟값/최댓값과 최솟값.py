def solution(s):
    answer = ''
    lst = list(s.split(" "))
    for i in range(len(lst)):
        lst[i] = int(lst[i])
        
    mn = str(min(lst))
    mx = str(max(lst))
    
    answer += mn
    answer += " "
    answer += mx
    
    return answer