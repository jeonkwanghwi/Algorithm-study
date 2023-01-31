slist = set([])
for i in range(1,11):
    comp = int(input())
    slist.add(comp%42)

print(len(slist))