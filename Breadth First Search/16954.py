from collections import deque

graph = [list(input()) for _ in range(8)]
wall = []

for i in range(8):
    for j in range(8):
        if graph[i][j]=='#':
            wall.append([i, j])

def update():
    global wall
    n_wall = []
    
    while wall:
        x, y = wall.pop()
        graph[x][y] = '.'
        
        if x<7:
            n_wall.append([x+1, y])
    
    for x, y in n_wall:
        graph[x][y] = '#'
    
    wall = n_wall

q = [deque([[7, 0]])]
cache = [[0]*8 for _ in range(8)]

dx = [0, -1, -1, -1, 1, 1, 1, 0, 0]
dy = [0, -1, 0, 1, -1, 0, 1, -1, 1]

while q[0]:
    q_q = q.pop()
    q.append(deque())
    
    while q_q:
        x, y = q_q.popleft()
        cache[x][y] = 0
        
        if x==0 and y==7:
            print(1)
            exit()
        
        for i in range(9):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx<0 or nx>7 or ny<0 or ny>7:
                continue
            
            if nx>0 and graph[nx-1][ny]=='#':
                continue
            
            if not cache[nx][ny] and graph[nx][ny]=='.':
                cache[nx][ny] = 1
                q[0].append([nx, ny])
    
    update()

print(0)
