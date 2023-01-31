n = int(input())
room_check = []

for i in range(n):
    a,b = map(int, input().split())
    room_check.append([a,b])

room_check.sort(key=lambda x:x[0])
room_check.sort(key=lambda x:x[1])

cnt = 1
end = room_check[0][1]
for i in range(1, n):
    if end <= room_check[i][0]:
        cnt += 1
        end = room_check[i][1]


print(cnt)