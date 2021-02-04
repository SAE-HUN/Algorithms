from collections import deque

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]

tmp = 0
for i in range(n):
    for j in range(m):
        if graph[i][j]=='S':
            x, y, z = i, j, 4
        if graph[i][j]=='C':
            if not tmp:
                tmp += 1
            else:
                graph[i][j] = 'D'

visited = [[[[[0]*2 for i in range(2)] for j in range(4)] for k in range(m)] for _ in range(n)]
queue = deque([[x, y, 4, 0, 0, 0]])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y, z, c, d, e = queue.popleft()
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        nz = i
        
        if nx<0 or nx>=n or ny<0 or ny>=m or nz==z:
            continue
        
        nc = c+(graph[nx][ny]=='C' and not c)
        nd = d+(graph[nx][ny]=='D' and not d)
        ne = e+1
        
        if nc and nd:
            print(ne)
            exit()
        
        if not visited[nx][ny][nz][nc][nd] and graph[nx][ny]!='#':
            visited[nx][ny][nz][nc][nd] = 1
            queue.append([nx, ny, nz, nc, nd, ne])

print(-1)
