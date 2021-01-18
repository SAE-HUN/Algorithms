from collections import deque

def MIS():
    return map(int, input().split())

def _int(a):
    return int(a)-1

def _MIS():
    return map(_int, input().split())

n, m, k = MIS()
graph = [list(MIS()) for _ in range(n)]

x, y = _MIS()
passengers = [list(_MIS()) for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1 , 1]

def bfs(x, y, a, b):
    cache = [[0]*n for _ in range(n)]
    cache[x][y] = 1
    queue = deque([[x, y]])
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            
            if type(a)==int and nx==a and ny==b:
                return cache[x][y]
            
            if not graph[nx][ny] and not cache[nx][ny]:
                cache[nx][ny] = cache[x][y]+1
                queue.append([nx, ny])
    
    return cache

while m:
    cache= bfs(x, y, False, False)
    passengers.sort(reverse=True, key=lambda x:(cache[x[0]][x[1]], x[0], x[1]))
    p = passengers.pop()
    dist = cache[p[0]][p[1]]
    
    if dist==0 or k<dist-1:
        print(-1)
        exit()
    
    k -= dist-1
    dist = bfs(p[0], p[1], p[2], p[3])
    
    if type(dist)!=int or k<dist:
        print(-1)
        exit()
    
    x, y = p[2], p[3]
    k += dist
    m -= 1

print(k)
