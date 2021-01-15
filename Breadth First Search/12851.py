from collections import deque

n, k = map(int, input().split())
cache = [0]*100001
cache[n] = 1
queue = deque([n])
count = 0

while queue:
    x = queue.popleft()
    
    if x==k:
        count += 1
        continue
    
    for a, b in [[2, 0], [1, -1], [1, 1]]:
        nx = a*x+b
        
        if nx<0 or nx>100000:
            continue
        
        if not cache[nx]:
            cache[nx] = cache[x]+1
        if cache[nx]==cache[x]+1:
            queue.append(nx)

print(cache[k]-1)
print(count)
