test = int(input())
for i in range(test):
    num, word = input().split()

    for j in word:
        for k in range(int(num)):
            print(j, end='')
    print()