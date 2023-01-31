h, m = map(int, input().split())

if m>=45 and m<=59:
    m=m-45
elif m>=0 and m<45:
    m=m+15
    h=h-1
    if h<0:
        h=h+24

print(h, m)