def isEmpty(s):
    if len(s) == 0:
        return True
    return False
    
def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else: # ")"
            if isEmpty(stack):
                return False
            stack.pop()
            
    if len(stack) == 0:
        return True
    return False