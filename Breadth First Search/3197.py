from collections import deque

def MIS():
    return map(int, input().split())

r, c = MIS()
lake = [list(input().strip()) for _ in range(r)]
swan = []
queue = deque()
cache = [[0]*c for _ in range(r)]

for i in range(r):
    for j in range(c):
        if lake[i][j]=='L':
            swan.append([i, j])
            lake[i][j] = '.'
        
        if lake[i][j]=='.':
            queue.append([i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
max_day = 0

while queue:
    x, y = queue.popleft()
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if nx<0 or nx>=r or ny<0 or ny>=c:
            continue
        
        if lake[nx][ny]=='X' and not cache[nx][ny]:
            cache[nx][ny] = cache[x][y]+1
            max_day = max(max_day, cache[nx][ny])
            queue.append([nx, ny])

x, y = swan[0]
a, b = swan[1]
queue = deque([[x, y]])
visited = [[0]*c for _ in range(r)]
visited[x][y] = 1
n_que = [[] for _ in range(max_day+1)]
answer = 0

def bfs():
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx<0 or nx>=r or ny<0 or ny>=c or visited[nx][ny]:
                continue
            
            if nx==a and ny==b:
                print(answer)
                exit()
            
            visited[nx][ny] = 1
            if cache[nx][ny]>answer:
                n_que[cache[nx][ny]].append([nx, ny])
                continue
            
            queue.append([nx, ny])

while True:
    bfs()
    answer += 1
    queue.extend(n_que[answer])
