from collections import deque

n, m = map(int, input().split())
miro = []

for _ in range(n):
    row = list(map(int, input().strip()))
    miro.append(row)

def bfs():
    queue = deque([[0, 0]])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            
            if miro[nx][ny]==1:
                miro[nx][ny] = miro[x][y]+1
                queue.append([nx, ny])

bfs()
print(miro[n-1][m-1])
