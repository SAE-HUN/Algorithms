from collections import deque

n, m = map(int, input().split())
iceberg = [[*map(int, input().split())] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

def get_count():
    count = 0
    visited = [[0]*m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and iceberg[i][j]:
                bfs(i, j, visited)
                count += 1
    
    return count

def bfs(x, y, visited):
    queue = deque([[x, y]])
    visited[x][y] = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            
            if not visited[nx][ny] and iceberg[nx][ny]:
                queue.append([nx, ny])
                visited[nx][ny] = 1

def update():
    cache = get_cache()
    
    for i in range(n):
        for j in range(m):
            iceberg[i][j] -= min(iceberg[i][j], cache[i][j])

def get_cache():
    cache = [[0]*m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if not iceberg[i][j]:
                continue
            
            count = 0
            for k in range(4):
                nx = i+dx[k]
                ny = j+dy[k]
                
                if nx<0 or nx>=n or ny<0 or ny>=m:
                    continue
                
                if not iceberg[nx][ny]:
                    count += 1
            cache[i][j] = count
    
    return cache

while True:
    count = get_count()
    
    if count>=2:
        break
    
    if not count:
        print(0)
        exit()
    
    update()
    answer += 1

print(answer)
