def solution(a, b, n):
    ans = 0
    while(True):
        if n<a:
            break
        ans += (n//a)*b
        n = (n//a)*b + n%a
        
    return ans