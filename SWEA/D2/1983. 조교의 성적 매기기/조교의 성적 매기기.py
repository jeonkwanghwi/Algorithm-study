t = int(input())
for test_case in range(t):
    n, k = map(int, input().split())
    students = []
    grade = ['D0', 'C-', 'C0', 'C+', 'B-', 'B0', 'B+', 'A-', 'A0', 'A+']
    for i in range(1, n+1):
        mid, final, hw = map(int, input().split())
        total = 0.35*mid + 0.45*final + 0.2*hw
        students.append((i, total)) # 순서랑 토탈값 같이 저장

    # 총점 기준으로 내림차순 정렬
    students.sort(key=lambda x: x[1])
    per_grade = n // 10 # 몇명씩 학점 줄지에 대한 단위

    for i in range(n):
        # students[i][1] = grade[i // per_grade] 이거는 튜플이라서 안됨
        students[i] = (students[i][0], grade[i // per_grade])

    for i in range(n):
        if students[i][0] == k:
            print(f"#{test_case+1}", students[i][1])
            break