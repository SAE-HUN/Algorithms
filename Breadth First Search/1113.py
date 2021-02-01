from collections import deque

n, m = map(int, input().split())

land = [[0]*(m+2)]
for _ in range(n):
    row = list(map(int, input().strip()))
    land.append([0]+row+[0])
land.append([0]*(m+2))

water = [[0]*(m+2) for _ in range(n+2)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    visited = [[0]*(m+2) for _ in range(n+2)]
    queue = deque([[x, y]])
    cache = [[x, y]]
    max_h = land[x][y]
    wall = 10
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx<0 or nx>=n+2 or ny<0 or ny>=m+2:
                continue
            
            if max_h>=land[nx][ny]:
                if not land[nx][ny] or water[nx][ny]==-1:
                    return False, []
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    cache.append([nx, ny])
                    queue.append([nx, ny])
            else:
                wall = min(wall, land[nx][ny])
    
    return wall, cache

def fill_water(wall, pool):
    for x, y in pool:
        water[x][y] = wall-land[x][y]

for i in range(n+2):
    for j in range(m+2):
        if not land[i][j]:
            water[i][j] = -1
        
        if not water[i][j]:
            wall, pool = bfs(i, j)
            
            if not wall:
                water[i][j] = -1
            else:
                fill_water(wall, pool)

answer = 0
for row in water:
    for w in row:
        answer += w*(w>0)
print(answer)
