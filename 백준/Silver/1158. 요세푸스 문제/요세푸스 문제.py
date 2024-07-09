n, k = map(int, input().split())
lst = [x+1 for x in range(n)]

removed_people = [] # 제거된 사람 모임
remv = 0 # 제거될 사람

for i in range(1, n+1):
    remv += (k-1)
    if remv >= len(lst):
        remv %= len(lst)
    removed_people.append(lst[remv])
    lst.pop(remv)

print("<",', '.join(map(str, removed_people)),">", sep="")
