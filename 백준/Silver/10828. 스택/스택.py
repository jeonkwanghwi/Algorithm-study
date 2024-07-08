
import sys
input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
    inst = input().split()

    if inst[0] == "push":
        stack.append(inst[-1])

    elif inst[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif inst[0] == "size":
        print(len(stack))

    elif inst[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif inst[0] == "top":
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])