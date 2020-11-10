n, k = map(int, input().split())
order = list(map(int, input().split()))
result = 0
current = []

for i in range(k):
    if order[i] in current:
        continue
    if len(current) < n:
        current.append(order[i])
        continue
    
    check = []
    for j in range(n):
        try:
            index = order[i:].index(current[j])
        except:
            index = 101
        check.append(index)
    
    a = check.index(max(check))
    del current[a]
    current.append(order[i])
    result += 1
print(result)
