def solution(num1, den1, num2, den2):
    answer = []
    tmp = den1
    num1 = num1 * den2
    den1 = den1 * den2
    
    num2 = num2 * tmp
    den2 = den2 * tmp
    
    total = num1 + num2
    
    m = max(den2, total)
    for i in range(m, 1, -1):
        if total % i == 0 and den2 % i == 0:
            den2 = den2 // i
            total = total // i
    
    answer.append(total)
    answer.append(den2)
    
    return answer