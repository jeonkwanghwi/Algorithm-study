def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        s = commands[i][0]-1 # 2 / 1
        e = commands[i][1] # 5 / 6
        point = commands[i][2]-1
        tmp = sorted(array[s:e])
        answer.append(tmp[point])
    
    return answer