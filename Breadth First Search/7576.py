from collections import deque

n, m = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(m)]

queue = deque()
for i in range(m):
    for j in range(n):
        if box[i][j]==1:
            queue.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while queue:
    x, y = queue.popleft()
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if nx<0 or nx>=m or ny<0 or ny>=n:
            continue
        
        if not box[nx][ny]:
            box[nx][ny] = box[x][y]+1
            queue.append((nx, ny))

answer = 1
for i in range(m):
    for j in range(n):
        if not box[i][j]:
            print(-1)
            exit()
        
        answer = max(answer, box[i][j])

print(answer-1)
