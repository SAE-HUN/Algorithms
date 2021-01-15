from collections import deque

k = int(input())
w, h = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]

cache = [[[0]*(k+1) for _ in range(w)] for j in range(h)]
cache[0][0][k] = 1
queue = deque([[0, 0, k]])

dx = [-1, 1, 0, 0, -2, -2, -1, -1, 1, 1, 2, 2]
dy = [0, 0, -1, 1, -1, 1, -2, 2, -2, 2, -1, 1]

while queue:
    x, y, z = queue.popleft()
    
    if x==h-1 and y==w-1:
        print(cache[x][y][z]-1)
        exit()
    
    for i in range(12):
        if i>3 and not z:
            break
        nx = x+dx[i]
        ny = y+dy[i]
        
        if nx<0 or nx>=h or ny<0 or ny>=w:
            continue
        
        if not cache[nx][ny][z-(i>3)] and not board[nx][ny]:
            cache[nx][ny][z-(i>3)] = cache[x][y][z]+1
            queue.append([nx, ny, z-(i>3)])

print(-1)
