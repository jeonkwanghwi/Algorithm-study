def solution(sent):
    sent = list(sent)
    stack = []
    for i in range(len(sent)):

        # 스택이 비어있으면 append
        if len(stack) == 0:
            stack.append(sent[i])
            continue

        if stack[-1] == sent[i]:
            stack.pop()
        else:
            stack.append(sent[i])
            
    if len(stack) == 0:
        return 1
    else:
        return 0