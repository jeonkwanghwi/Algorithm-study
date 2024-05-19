def solution(keymap, targets):
    d = dict()
    result = []

    for i in keymap:
        for target in i:
            if target in d:  # 값이 이미 있을 때
                d[target] = min(i.index(target) + 1, d[target])
            else:  # 값을 처음 넣는 경우
                d[target] = i.index(target) + 1

    for i in targets:
        print("i", i)
        sum = 0
        for target in i:
            if target not in d:
                sum = -1
                break
            else:
                sum += d[target]
                print("점검", target, sum)
        print("sum", sum)
        result.append(sum)

    return result


print(solution(["BC"],["CAC","BC"]))