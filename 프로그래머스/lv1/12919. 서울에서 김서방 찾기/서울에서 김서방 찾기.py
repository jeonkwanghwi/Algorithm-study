def solution(seoul):
    answer = 0
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            answer += i
    
    return f"김서방은 {answer}에 있다"