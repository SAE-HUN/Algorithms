import heapq

n = int(input())
home = [list(input()) for _ in range(n)]

def find_door():
    for i in range(n):
        for j in range(n):
            if home[i][j]=='#':
                return i, j

x, y = find_door()
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

queue = []
visited = [[[0]*4 for i in range(n)] for _ in range(n)]

for i in range(4):
    queue.append([0, x, y, i])
    visited[x][y][i] = 1

while queue:
    mirror, x, y, i = heapq.heappop(queue)
    visited[x][y][i] = 1
    
    nx = x+dx[i]
    ny = y+dy[i]
    
    if nx<0 or nx>=n or ny<0 or ny>=n:
        continue
    
    if not visited[nx][ny][i] and home[nx][ny]=='#':
        print(mirror)
        exit()
    
    if not visited[nx][ny][i] and home[nx][ny]!='*':
        visited[nx][ny][i] = 1
        heapq.heappush(queue, [mirror, nx, ny, i])
    
    if home[nx][ny]=='!':
        for j in [-1, 1]:
            k = i+j
            k += 4*(k==-1)
            k *= (k!=4)
            
            if not visited[nx][ny][k]:
                heapq.heappush(queue, [mirror+1, nx, ny, k])
