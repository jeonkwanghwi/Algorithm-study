def solution(sizes):
    w = []
    h = []
    for i in range(len(sizes)):
        if sizes[i][0] > sizes[i][1]: # 가로가 더 길다면
            w.append(sizes[i][0])
            h.append(sizes[i][1])
        else:
            h.append(sizes[i][0])
            w.append(sizes[i][1])

    return max(w) * max(h)