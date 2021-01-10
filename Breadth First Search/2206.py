from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]

visit = []
for i in range(n):
    row = []
    for j in range(m):
        row.append([0, 0])
    visit.append(row)
visit[0][0][1] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
queue.append(((0, 0), 1))
while queue:
    (x, y), wall = queue.popleft()
    
    if x==n-1 and y==m-1:
        print(visit[x][y][wall])
        exit()
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        
        if not visit[nx][ny][wall] and not graph[nx][ny]:
            queue.append(((nx, ny), wall))
            visit[nx][ny][wall] = visit[x][y][wall]+1
        elif graph[nx][ny] and wall:
            queue.append(((nx, ny), wall-1))
            visit[nx][ny][wall-1] = visit[x][y][wall]+1

print(-1)
