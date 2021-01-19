from collections import deque

r, c = map(int, input().split())
cave = [list(input()) for _ in range(r)]
n = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, visited):
    cluster = [[x, y]]
    bottom = [-1]*c
    min_h = x
    
    queue = deque([[x, y]])
    visited[x][y] = 1
    
    while queue:
        x, y = queue.popleft()
        
        if bottom[y]<x:
            bottom[y] = x
        
        if x>min_h:
            min_h = x
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx<0 or nx>=r or ny<0 or ny>=c or visited[nx][ny]:
                continue
            
            if cave[nx][ny]=='x':
                visited[nx][ny] = 1
                cluster.append([nx, ny])
                queue.append([nx, ny])
    
    return cluster, bottom, min_h

def divide(x, y):
    visited = [[0]*c for _ in range(r)]
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if nx<0 or nx>=r or ny<0 or ny>=c or visited[nx][ny] or cave[nx][ny]=='.':
            continue
        
        cluster, bottom, min_h = bfs(nx, ny, visited)
        
        if min_h!=r-1:
            return cluster, bottom
    
    return False

def down(cluster, bottom):
    min_dist = r-1
    for y, x in enumerate(bottom):
        if x==-1:
            continue
        
        dist = 0
        x +=1
        
        while x<r and cave[x][y]!='x':
            dist += 1
            x += 1
        
        min_dist = min(min_dist, dist)
    
    for x, y in cluster:
        cave[x][y] = '.'
    
    for x, y in cluster:
        cave[x+min_dist][y] = 'x'

for i, h in enumerate(map(int, input().split())):
    x = r-h
    y = 0+(c-1)*(i%2)
    d = -2*(i%2)+1
    
    while 0<=y<c:
        if cave[x][y]=='.':
            y += d
            continue
        
        cave[x][y] = '.'
        result = divide(x, y)
        
        if result!=False:
            down(*result)
        
        break

for row in cave:
    for cell in row:
        print(cell, end='')
    print()
