def solution(age):
    answer = ''
    
    age = str(age)
    for i in age:
        answer += chr(ord("a") + int(i))
    return answer