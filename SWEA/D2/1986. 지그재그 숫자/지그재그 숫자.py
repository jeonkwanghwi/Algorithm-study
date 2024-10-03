# 홀 : 더하기
# 짝 : 빼기
t = int(input())
for test_case in range(t):
    summ = 0
    n = int(input())
    for i in range(1, n+1):
        if i % 2 != 0:
            summ += i
        else:
            summ -= i
    print(f"#{test_case+1}", summ)