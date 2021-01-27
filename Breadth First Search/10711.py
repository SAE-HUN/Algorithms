from collections import deque

def MIS():
    return map(int, input().split())

h, w = MIS()
castle = [list(input()) for _ in range(h)]

dx = [-1, -1, -1, 1, 1, 1, 0, 0]
dy = [-1, 0, 1, -1, 0, 1, -1, 1]

def is_collapse(x, y):
    if castle[x][y]=='.':
        return False
    
    cnt = 0
    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if nx<0 or nx>=h or ny<0 or ny>=w:
            continue
        
        if castle[nx][ny]=='.':
            cnt += 1
    
    if int(castle[x][y])<=cnt:
        return True
    else:
        return False

queue = deque()
for i in range(h):
    for j in range(w):
        if is_collapse(i, j):
            queue.append([i, j])

answer = 0
cache = [[-1]*w for _ in range(h)]
while queue:
    answer += 1
    
    for i in range(len(queue)):
        x, y = queue[i]
        castle[x][y] = '.'
    
    for _ in range(len(queue)):
        x, y = queue.popleft()
        
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx<0 or nx>=h or ny<0 or ny>=w:
                continue
            
            if cache[nx][ny]!=answer and is_collapse(nx, ny):
                cache[nx][ny] = answer
                queue.append([nx, ny])

print(answer)
