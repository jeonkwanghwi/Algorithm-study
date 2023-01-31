import sys

a, b = map(int, sys.stdin.readline().strip().split())
total = a+b

A = list(map(int, sys.stdin.readline().strip().split()))
B = list(map(int, sys.stdin.readline().strip().split()))

settotal = set(A+B)
inter = total - len(settotal)

print(total - inter - inter)