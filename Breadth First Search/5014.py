from collections import deque
 
f, s, g, u, d = map(int, input().split())
cache = [0]*(f+1)
cache[s] = 1
queue = deque([s])
 
while queue:
    x = queue.popleft()
 
    if x==g:
        print(cache[x]-1)
        exit()
 
    for _d in [u, -d]:
        nx = x+_d
 
        if nx<1 or nx>f:
            continue
 
        if not cache[nx]:
            cache[nx] = cache[x]+1
            queue.append(nx)
 
print('use the stairs')
