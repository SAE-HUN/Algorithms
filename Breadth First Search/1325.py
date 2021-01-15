from collections import deque

def bfs(x):
    cache = [0]*(n+1)
    cache[x] = 1
    count = 1
    queue = deque([x])
    
    while queue:
        x = queue.popleft()
        
        for nx in graph[x]:
            if nx<1 or nx>n:
                continue
            
            if not cache[nx]:
                count += 1
                cache[nx] = 1
                queue.append(nx)
    
    return count

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

max_hack = 0
answer = [0]*(n+1)

for i in range(1, n+1):
    hack = bfs(i)
    answer[i] = hack
    max_hack = max(max_hack, hack)

for i in range(n):
    if answer[i+1]==max_hack:
        print(i+1, end=' ')
