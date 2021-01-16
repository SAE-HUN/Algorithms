from collections import deque
from itertools import combinations

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
count = 2

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, num):
    queue = deque([[x, y]])
    graph[x][y] = num
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            
            if graph[nx][ny]==1:
                graph[nx][ny] = num
                queue.append([nx, ny])

for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            bfs(i, j, count)
            count += 1

count -= 2
cache = [[10000]*count for _ in range(count)]

def is_outside(x, y):
    if not graph[x][y]:
        return False
    
    outside = []
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        
        if not graph[nx][ny]:
            outside.append([dx[i], dy[i]])
    
    return outside

def build(outside, x, y):
    _from  = graph[x][y]-2
    for dx, dy in outside:
        nx = x+dx
        ny = y+dy
        length = 1
        
        while True:
            nx += dx
            ny += dy
            
            if nx<0 or nx>=n or ny<0 or ny>=m:
                break
            
            if graph[nx][ny]:
                if length<2 or graph[nx][ny]==_from:
                    break
                
                to = graph[nx][ny]-2
                cache[_from][to] = min(cache[_from][to], length)
                cache[to][_from] = min(cache[to][_from], length)
                break
            
            length += 1

for i in range(n):
    for j in range(m):
        outside = is_outside(i, j)
        
        if not outside:
            continue
        
        build(outside, i, j)

bridges = []
check = [0]*count
for i in range(count):
    for j in range(count):
        if cache[i][j]==10000:
            continue
        bridges.append([i, j, cache[i][j]])
        cache[j][i] = 10000
        check[i] = 1
        check[j] = 1

if len(bridges)<count-1:
    print(-1)
    exit()

for i in range(count):
    if not check[i]:
        print(-1)
        exit()

bridge_combi = combinations(bridges, count-1)
answer = 100000

for a in bridge_combi:
    graph = [[] for _ in range(count)]
    check = [0]*count
    length = 0
    
    for x, y, l in a:
        length += l
        graph[x].append(y)
        graph[y].append(x)
    
    queue = deque([x])
    check[x] = 1
    
    while queue:
        x = queue.popleft()
        
        for nx in graph[x]:
            if not check[nx]:
                check[nx] = 1
                queue.append(nx)
    
    if not check.count(0):
        answer = min(answer, length)

print(answer if answer!=100000 else -1)
