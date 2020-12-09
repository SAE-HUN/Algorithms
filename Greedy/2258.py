def MIS():
    return map(int, input().split())

n, x = MIS()
sum_weight, costs, meats = 0, [], []

for _ in range(n):
    w, c = MIS()
    sum_weight += w
    meats.append((w, c))
    costs.append(c)

if sum_weight<x:
    print(-1)
    exit()

costs = sorted(list(set(costs))); costs.append(2147483648)
meats.sort(key=lambda x:(x[1], -x[0]))

l, r = 0, 2147483647
while l<r:
    mid = (l+r)//2
    
    if mid<costs[0]:
        l = mid+1
        continue
    
    for i, cost in enumerate(costs):
        if cost>mid:
            cost = costs[i-1]
            break
    
    sum_weight = 0
    for i, (w, c) in enumerate(meats):
        sum_weight += w
        if c==cost:
            break
    
    mid -= cost
    i += 1
    while i<n and meats[i][1]<=mid:
        sum_weight += meats[i][0]
        mid -= meats[i][1]
        i += 1
    
    if sum_weight<x:
        l = (l+r)//2+1
    else:
        r = (l+r)//2

print(l)
