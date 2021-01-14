from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
count = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def _bfs(x, y, num):
    queue = deque([[x, y]])
    visited[x][y] = 1
    graph[x][y] = num
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            
            if not visited[nx][ny] and graph[nx][ny]:
                queue.append([nx, ny])
                visited[nx][ny] = 1
                graph[nx][ny] = num

def is_outside(x, y):
    if not graph[x][y]:
        return False
    
    flag = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        
        if not visited[nx][ny] and not graph[nx][ny]:
            visited[nx][ny] = 1
            flag = 1
    
    return flag

def bfs(x, y, _from):
    queue = deque([[x, y]])
    visited = [[0]*n for _ in range(n)]
    cache = [[0]*n for _ in range(n)]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            
            if graph[nx][ny] and graph[nx][ny]!=_from:
                return cache[x][y]
            
            if not visited[nx][ny] and not graph[nx][ny]:
                queue.append([nx, ny])
                visited[nx][ny] = 1
                cache[nx][ny] = cache[x][y]+1
    
    return 10000

for i in range(n):
    for j in range(n):
        if graph[i][j] and not visited[i][j]:
            _bfs(i, j, count)
            count += 1

answer = 10000
for i in range(n):
    for j in range(n):
        if is_outside(i, j):
            answer = min(answer, bfs(i, j, graph[i][j]))

print(answer)
