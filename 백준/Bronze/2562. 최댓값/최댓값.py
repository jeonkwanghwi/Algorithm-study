max = 0
order = 1

for i in range(1,10):
    comp = int(input())
    if max < comp:
        max = comp
        order = i

print(max)
print(order)