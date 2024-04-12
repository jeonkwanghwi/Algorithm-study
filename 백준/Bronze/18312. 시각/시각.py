h, k = input().split()
m = 0
s = 0
cnt = 0
total = ""

for x in range(0, int(h) + 1):
    if x < 10:
        x = "0"+str(x)

    for y in range(0, 60):
        if y < 10:
            y = "0" + str(y)

        for z in range(0, 60):
            if z < 10:
                z = "0" + str(z)

            total = str(x)+str(y)+str(z)
            if k in total:
                cnt += 1
print(cnt)