from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]

cache = [[0]*m for _ in range(n)]
counts = [0]
num = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, num):
    cache[x][y] = num
    queue = deque([[x, y]])
    cnt = 0
    
    while queue:
        x, y = queue.popleft()
        cnt += 1
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            
            if not cache[nx][ny] and not graph[nx][ny]:
                cache[nx][ny] = num
                queue.append([nx, ny])
    
    counts.append(cnt)

for i in range(n):
    for j in range(m):
        if not cache[i][j] and not graph[i][j]:
            bfs(i, j, num)
            num += 1

def get_count(x, y):
    cnt = 1
    temp = []
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        
        num = cache[nx][ny]
        if not graph[nx][ny] and not num in temp:
            cnt += counts[num]
            temp.append(num)
        
    return cnt%10

for i in range(n):
    for j in range(m):
        if graph[i][j]:
            graph[i][j] = get_count(i, j)
        
        print(graph[i][j], end='')
    print()
