def solution(n, lost, reserve):
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)
    
    for i in new_lost:
        if i-1 in new_reserve: # 앞사람에게 빌림
            new_reserve.remove(i-1)
        elif i+1 in new_reserve: # 뒷사람에게 빌림
            new_reserve.remove(i+1)
        else:
            n-=1
    return n