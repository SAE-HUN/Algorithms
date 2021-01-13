from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(_x):
    queue = deque([_x])
    cache = [0]*(n+1)
    d = [-1, 1]
    
    while queue:
        x = queue.popleft()
        
        for nx in graph[x]:
            if nx<1 or nx>n:
                continue
            
            if not cache[nx]:
                cache[nx] = cache[x]+1
                queue.append(nx)
    
    cache[_x] = 0
    return cache

def get_kevin(cache):
    kevin = 0
    for i, a in enumerate(cache):
        kevin += a
    
    return kevin

answer = [None, 10000]
for i in range(n):
    cache = dfs(i+1)
    kevin = get_kevin(cache)
    
    if kevin<answer[1]:
        answer = [i+1, kevin]
    if kevin==answer[1]:
        answer[0] = min(answer[0], i+1)

print(answer[0])
