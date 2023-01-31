word = input() # baekjoon
alpha = [-1 for _ in range(26)]
order = 0
for i in word:
    for j in range(97, 123):
        if alpha[j-97] != -1:
            continue
        if ord(i) == j:
            alpha[j - 97] = order
    order += 1

for _ in alpha:
    print(_, end=' ')