for _ in range(int(input())):
    lst = input().split()
    for i in range(len(lst)):
        lst[i] = lst[i][::-1]
        print(lst[i], end=' ')
    print()