from collections import deque

def MIS():
    return map(int, input().split())

n, m, k = MIS()
graph = [list(map(int, input().strip())) for _ in range(n)]

cache = [[[0]*(k+1) for i in range(m)] for _ in range(n)]
cache[0][0][k] = 1
queue = deque([[0, 0, k, 0, 1]])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y, z, w, d = queue.popleft()
    
    if x==n-1 and y==m-1:
        print(d)
        exit()
    
    nw = -w+1
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        
        if graph[nx][ny]:
            if z and not cache[nx][ny][z-1]:
                if not w:
                    cache[nx][ny][z-1] = 1
                    queue.append([nx, ny, z-1, nw, d+1])
                else:
                    queue.append([x, y, z, nw, d+1])
        
        if not graph[nx][ny]:
            if not cache[nx][ny][z]:
                cache[nx][ny][z] = 1
                queue.append([nx, ny, z, nw, d+1])

print(-1)
