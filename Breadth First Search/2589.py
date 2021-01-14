from collections import deque

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    max_dist = 0
    cache = [[0]*m for _ in range(n)]
    cache[x][y] = 1
    queue = deque([[x, y]])
    
    while queue:
        x, y = queue.popleft()
        max_dist = max(max_dist, cache[x][y]-1)
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            
            if not cache[nx][ny] and graph[nx][ny]=='L':
                cache[nx][ny] = cache[x][y]+1
                queue.append([nx, ny])
    
    return max_dist

answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j]=='L':
            answer = max(answer, bfs(i, j))

print(answer)
