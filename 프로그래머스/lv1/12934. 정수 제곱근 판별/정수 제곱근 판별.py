import math
def solution(n):
    answer = 0
    
    nn = int(math.sqrt(n))
    
    if nn * nn == n:
        return (nn+1) ** 2
    else:
        return -1
