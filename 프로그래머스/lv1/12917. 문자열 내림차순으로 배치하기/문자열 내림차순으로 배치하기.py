def solution(s):
    s = list(s)
    s.sort(reverse = True)
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) == 32 and ord(s[i-1]) > ord(s[i]):
            s[i-1], s[i] = s[i], s[i-1]
            
    
    return "".join(s)