import sys

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

y, d = 0, 0
visited = [0]*n

def dfs(x, depth):
    global y, d, visited
    
    if d==4:
        return
    
    if depth>d:
        y = x
        d = depth
    
    for nx in graph[x]:
        if not visited[nx]:
            visited[nx] = 1
            dfs(nx, depth+1)
            visited[nx] = 0

visited[y] = 1
dfs(y, 0)
visited[y] = 0

if d>=4:
    print(1)
    exit()
else:
    visited = [0]*n
    visited[y] = 1
    dfs(y, 0)

if d>=4:
    print(1)
else:
    print(0)
