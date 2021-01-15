from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    cache = [[0]*w for _ in range(h)]
    
    for i in range(h):
        for j in range(w):
            if building[i][j]=='*':
                queue.append([i, j, True])
            
            if building[i][j]=='@':
                x, y = i, j
    
    queue.append([x, y, False])
    
    while queue:
        x, y, fire = queue.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx<0 or nx>=h or ny<0 or ny>=w:
                if not fire:
                    return cache[x][y]+1
                continue
            
            if not cache[nx][ny] and building[nx][ny]=='.':
                cache[nx][ny] = cache[x][y]+1
                queue.append([nx, ny, fire])
    
    return 'IMPOSSIBLE'

t = int(input())

while t:
    w, h = map(int, input().split())
    building = [list(input()) for _ in range(h)]
    
    print(bfs())
    t -= 1
