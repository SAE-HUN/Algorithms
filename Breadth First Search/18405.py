from collections import deque

def MIS():
    return map(int, input().split())

n, k = MIS()
tube = [list(MIS()) for _ in range(n)]
s, X, Y = MIS()

queue = []
for i in range(n):
    for j in range(n):
        z = tube[i][j]
        
        if z:
            queue.append([z, i, j])

queue.sort()
queue = deque(queue)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while s>0:
    if not queue:
        break
    
    for _ in range(len(queue)):
        z, x, y = queue.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            
            if not tube[nx][ny]:
                tube[nx][ny] = z
                queue.append([z, nx, ny])
    
    queue = deque(sorted(queue))
    s -=1

print(tube[X-1][Y-1])
