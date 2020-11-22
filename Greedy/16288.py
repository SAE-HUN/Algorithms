n, k = map(int, input().split())
queue = list(map(int, input().split()))

counters = []
for _ in range(k):
    counters.append([0])

for passenger in queue:
    temp = None
    min_diff = 99
    
    for counter in counters:
        diff = passenger - counter[-1]
        
        if diff>0 and diff<min_diff:
            min_diff = diff
            temp = counter
    
    if min_diff<99:
        temp.append(passenger)
    else:
        print('NO')
        exit()

print('YES')
