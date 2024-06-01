def solution(a, b):
    if a > b:
        a, b = b, a
    return sum([x for x in range(a, b+1)])