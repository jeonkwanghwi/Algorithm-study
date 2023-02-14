n = int(input())
room = []

for i in range(n):
    a = list(map(int, input().split()))
    room.append(a)


# 처음에는 끝나는 시간인 room[i][1]에 대해서만 정렬하면 된다고 생각했음.
# 근데 회의 시작시간을 고려하지 않으면 3 3 / 2 3일 경우에 1로 나와버림
room.sort(key=lambda x:x[0])
room.sort(key=lambda x:x[1])

end = room[0][1] # 맨 처음 회의가 끝나는 시간
cnt = 1 # 회의는 최소 1개
for i in range(1, n):
    if end <= room[i][0]:
        cnt += 1
        end = room[i][1]

print(cnt)