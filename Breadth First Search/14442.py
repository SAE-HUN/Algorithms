from collections import deque

n, m, k = map(int, input().split())
graph = [[*map(int, list(input()))] for _ in range(n)]

cache = [[[0]*(k+1) for i in range(m)] for _ in range(n)]
cache[0][0][k] = 1
queue = deque([[0, 0, k]])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y, w = queue.popleft()
    
    if x==n-1 and y==m-1:
        print(cache[x][y][w])
        exit()
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        
        if graph[nx][ny] and w and not cache[nx][ny][w-1]:
            cache[nx][ny][w-1] = cache[x][y][w]+1
            queue.append([nx, ny, w-1])
        
        if not graph[nx][ny] and not cache[nx][ny][w]:
            cache[nx][ny][w] = cache[x][y][w]+1
            queue.append([nx, ny, w])

print(-1)
