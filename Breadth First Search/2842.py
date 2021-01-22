from collections import deque

n = int(input())
town = [list(input()) for _ in range(n)]
height = [list(map(int, input().split())) for _ in range(n)]

house = 0
_height = set()
for i in range(n):
    for j in range(n):
        _height.add(height[i][j])
        
        if town[i][j]=='K':
            house += 1
        if town[i][j]=='P':
            a, b = i, j

_height = sorted(_height)
end = 0
answer = 1000000

dx = [-1, -1, -1, 1, 1, 1, 0, 0]
dy = [-1, 0, 1, -1, 0, 1, -1, 1]

def bfs(min_h, max_h):
    queue = deque([[a, b]])
    visited = [[0]*n for _ in range(n)]
    visited[a][b] = 1
    k = 0
    
    while queue and k<house:
        x, y = queue.popleft()
        
        if town[x][y]=='K':
            k += 1
        
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            
            if not visited[nx][ny] and min_h<=height[nx][ny]<=max_h:
                visited[nx][ny] = 1
                queue.append([nx, ny])
    
    return k

for start in range(len(_height)):
    min_h = _height[start]
    
    while end<len(_height):
        max_h = _height[end]
        
        k = bfs(min_h, max_h)
    
        if k==house and min_h<=height[a][b]<=max_h:
            answer = min(answer, max_h-min_h)
            break
        else:
            end += 1

print(answer)
