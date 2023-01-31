a = int(input())
cycle = 0 # 횟수

if a<10:
    a=a*10

newnum = (a % 10) * 10 + (a//10 + a%10)%10
cycle += 1

while a!=newnum:
    newnum = (newnum % 10) * 10 + (newnum // 10 + newnum % 10) % 10
    cycle += 1

print(cycle)