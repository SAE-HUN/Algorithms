from collections import deque

n = int(input())
flat = [list(input()) for _ in range(n)]

def get_dir(x, y, cell):
    if cell=='0' or cell=='1':
        return False
    
    hor = 0
    try:
        hor = flat[x-1][y]==flat[x][y]==flat[x+1][y]
    except:
        pass
    
    ver = 0
    try:
        ver = flat[x][y-1]==flat[x][y]==flat[x][y+1]
    except:
        pass
    
    return 2*hor+ver

for i in range(n):
    for j in range(n):
        _dir = get_dir(i, j, flat[i][j])
        
        if _dir:
            _dir -= 1
            if flat[i][j]=='B':
                x, y, z = i, j, _dir
            else:
                a, b, c = i, j, _dir

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def can_move(x, y, z):
    for d in [-1, 0, 1]:
        nx = x+d*z
        ny = y+d*(not z)
        
        if nx<0 or nx>=n or ny<0 or ny>=n:
            return False
        
        if flat[nx][ny]=='1':
            return False
    
    return True

def can_rotate(x, y):
    dx = [-1, -1, -1, 1, 1, 1, 0, 0]
    dy = [-1, 0, 1, -1, 0, 1, -1, 1]
    
    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if nx<0 or nx>=n or ny<0 or ny>=n:
            return False
        
        if flat[nx][ny]=='1':
            return False
    
    return True

cache = [[[0]*2 for i in range(n)] for _ in range(n)]
cache[x][y][z] = 1
queue = deque([[x, y, z]])

while queue:
    x, y, z = queue.popleft()
    
    if x==a and y==b and z==c:
        print(cache[a][b][c]-1)
        exit()
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if can_move(nx, ny, z):
            if cache[nx][ny][z]:
                continue
            
            cache[nx][ny][z] = cache[x][y][z]+1
            queue.append([nx, ny, z])
    
    if can_rotate(x, y):
        if cache[x][y][-z+1]:
            continue
        
        cache[x][y][-z+1] = cache[x][y][z]+1
        queue.append([x, y, -z+1])

print(0)
