def factorial(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return factorial(n-2) + factorial(n-1)

n = int(input())

print(factorial(n))