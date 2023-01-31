c=int(input())
for i in range(c): #(1)
    li=list(map(int,input().split()))
    c=0
    for j in li[1:]: #(2)
        avg=sum(li[1:])/li[0]
        if j>avg:
            c+=1
    rate=c/li[0]*100
    print('{0:0.3f}%'.format(rate))