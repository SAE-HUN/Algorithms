from collections import deque

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def dfs(x, y):
    cache = [[x, y]]
    value = graph[x][y]
    queue = deque([[x, y]])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            
            if not visited[nx][ny] and l<=abs(graph[nx][ny]-graph[x][y])<=r:
                queue.append([nx, ny])
                cache.append([nx, ny])
                visited[nx][ny] = 1
                value += graph[nx][ny]
    
    return cache, value//len(cache)

def update(caches, values):
    for i, cache in enumerate(caches):
        for x, y in cache:
            graph[x][y] = values[i]

while True:
    visited = [[0]*n for _ in range(n)]
    caches = []
    values = []
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = 1
                cache, value = dfs(i, j)
                
                if len(cache)==1:
                    continue
                
                caches.append(cache)
                values.append(value)
    
    if caches:
        update(caches, values)
        answer += 1
    else:
        break

print(answer)
