def solution(arr1, arr2):
    answer = []
    
    n = len(arr1)
    m = len(arr1[0])
    print(n, m)
    
    for i in range(n):
        tmp = []
        for j in range(m):
            tmp.append(arr1[i][j] + arr2[i][j])
        answer.append(tmp)
    
    return answer