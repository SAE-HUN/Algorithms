from collections import deque

r, c = map(int, input().split())
forest = [list(input().strip()) for _ in range(r)]
queue = deque()

for i in range(r):
    for j in range(c):
        if forest[i][j]=='*':
            queue.append([i, j, '*'])
        if forest[i][j]=='S':
            hx, hy = i, j
            forest[i][j] = '.'

queue.append([hx, hy, 0])
cache = [[0]*c for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y, w = queue.popleft()
    
    if forest[x][y]=='D':
        print(cache[x][y])
        exit()
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if nx<0 or nx>=r or ny<0 or ny>=c:
            continue
        
        if w:
            if forest[nx][ny]=='.':
                forest[nx][ny] = '*'
                queue.append([nx, ny, w])
        else:
            if not cache[nx][ny] and (forest[nx][ny]=='.' or forest[nx][ny]=='D'):
                cache[nx][ny] = cache[x][y]+1
                queue.append([nx, ny, w])

print('KAKTUS')
