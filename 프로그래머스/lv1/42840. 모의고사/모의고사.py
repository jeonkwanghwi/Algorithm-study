def solution(answers):
    first = [1, 2, 3, 4, 5] * 2000
    first_score = 0

    second = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    second_score = 0

    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    third_score = 0

    for i in range(len(answers)):
        if answers[i] == first[i]:
            first_score += 1
        if answers[i] == second[i]:
            second_score += 1
        if answers[i] == third[i]:
            third_score += 1

    score = [first_score, second_score, third_score]
    result = []

    for i in range(len(score)):
        if max(score) == score[i]:
            result.append(i + 1)

    return result