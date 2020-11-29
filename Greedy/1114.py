l, k, c = map(int, input().split())
locs = [0, l]

for loc in map(int, input().split()):
    locs.append(loc)
locs.sort()

left, right = 0, 1000000000
while left<right:
    mid = (left+right)//2
    cut, diff = 0, 0
    
    for i in range(k, -1, -1):
        diff += locs[i+1] - locs[i]
        if diff>mid:
            cut += 1
            diff = locs[i+1] - locs[i]
            if diff>mid:
                cut = c+1
                break
    
    flag = cut>c
    
    if flag:
        left = mid+1
    else:
        right = mid

cut, diff, idx = 0, 0, k
for i in range(k, -1, -1):
    diff += locs[i+1] - locs[i]
    if diff>left:
        cut += 1
        diff = locs[i+1] - locs[i]
        idx = i+1

if cut<c: idx = 1
print(left, locs[idx])
