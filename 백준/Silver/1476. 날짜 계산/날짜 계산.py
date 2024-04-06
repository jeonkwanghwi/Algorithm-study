e,s,m = map(int, input().split())
a = 0
b = 0
c = 0
year = 0

while a!=e or b!=s or c!=m:
    a += 1
    b += 1
    c += 1
    year += 1
    
    if a > 15:
        a = 1
    if b > 28:
        b = 1
    if c > 19:
        c = 1
print(year)