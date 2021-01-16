from collections import deque
 
def MIS():
    return map(int, input().split())
 
m, n = MIS()
factory = [[*MIS()] for _ in range(m)]
x, y, z = MIS()
a, b, c = MIS()
 
cache = [[[0]*4 for i in range(n)] for _ in range(m)]
queue = deque([[x-1, y-1, z-1]])
cache[x-1][y-1][z-1] = 1
d = [[1, 0], [2, 0], [3, 0], [0, 1], [0, 2]]
 
while queue:
    x, y, z = queue.popleft()
 
    if x==a-1 and y==b-1 and z==c-1:
        print(cache[x][y][z]-1)
        exit()
 
    for k, _dir in d:
        dx = k*((z==2)-(z==3))
        dy = k*((z==0)-(z==1))
        dz = (_dir+(z==3 or z==0))*(2*(z<2)-1)*(bool(_dir))
        
        nx = x+dx
        ny = y+dy
        nz = z+dz
 
        if nx<0 or nx>=m or ny<0 or ny>=n:
            continue
        
        flag = 0
        for tmp in range(abs(dx)):
            tmp += 1
            tmp *= 2*(dx>0)-1
            if factory[x+tmp][y]:
                flag = 1
                break
        
        for tmp in range(abs(dy)):
            tmp += 1
            tmp *= 2*(dy>0)-1
            if factory[x][y+tmp]:
                flag = 1
                break
        
        if flag:
            continue
 
        if not cache[nx][ny][nz]:
            cache[nx][ny][nz] = cache[x][y][z]+1
            queue.append([nx, ny, nz])
