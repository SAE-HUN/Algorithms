from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def can_build(x, y):
    if graph[x][y]:
        return False
    
    udlr = []
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if nx<0 or nx>=n or ny<0 or ny>=n:
            udlr.append(1)
            continue
        
        udlr.append(graph[nx][ny])
    
    if 0 in udlr[:2] and 0 in udlr[2:]:
        return False
    
    return True

def bfs():
    visited = [[0]*n for _ in range(n)]
    visited[0][0] = 1
    queue = deque([[0, 0]])
    time = 0
    
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            
            if x==n-1 and y==n-1:
                return time
            
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                
                if nx<0 or nx>=n or ny<0 or ny>=n:
                    continue
                
                if visited[nx][ny] or not graph[nx][ny]:
                    continue
                
                if graph[x][y]>1 and graph[nx][ny]>1:
                    continue
                
                if graph[nx][ny]==1:
                    visited[nx][ny] = 1
                    queue.append([nx, ny])
                elif graph[nx][ny]>1:
                    if not (time+1)%graph[nx][ny]:
                        visited[nx][ny] = 1
                        queue.append([nx, ny])
                    else:
                        queue.append([x, y])
        
        time += 1

time = bfs()
if time:
    answer = time
else:
    answer = 1000000000

for i in range(n):
    for j in range(n):
        if can_build(i, j):
            graph[i][j] = m
            time = bfs()
            if time:
                answer = min(answer, time)
            graph[i][j] = 0

print(answer)
