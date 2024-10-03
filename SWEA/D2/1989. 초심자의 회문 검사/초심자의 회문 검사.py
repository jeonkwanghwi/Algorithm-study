t = int(input())
for test_case in range(t):
    word = input()
    check = 1
    for i in range(len(word)):
        if word[i] != word[-(i+1)]:
            check = 0
            break

    print(f"#{test_case+1}", check)