n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
A.sort()
length = len(A)


for i in range(m):
    target = B[i]
    flag = 0
    left = 0
    right = length - 1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == target:
            flag = 1
            print(1)
            break
        elif A[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    if flag == 0:
        print(0)