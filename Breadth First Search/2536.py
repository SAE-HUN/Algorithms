from collections import deque

n, m = map(int, input().split())
k = int(input())
bus = []

for _ in range(k):
    a, sx, sy, dx, dy = map(int, input().split())
    bus.append(sorted([[sx, sy], [dx, dy]]))

def can_take(i, x, y):
    (sx, sy), (dx, dy) = bus[i]
    
    if sx==dx==x and sy<=y<=dy:
        return True
    
    if sy==dy==y and sx<=x<=dx:
        return True
    
    return False

def can_transfer(i, j):
    (a, b), (c, d) = bus[i]
    (e, f), (g, h) = bus[j]
    
    if e<=a==c<=g and b<=f==h<=d:
        return True
    
    if f<=b==d<=h and a<=e==g<=c:
        return True
    
    if a==c==e==g and (b<=f<=d or f<=b<=h):
        return True
    
    if b==d==f==h and (a<=e<=c or e<=a<=g):
        return True
    
    return False
    

sx, sy, dx, dy = map(int, input().split())
queue = deque()
visited = [0]*k
graph = [[] for _ in range(k)]
end = [0]*k

for i in range(k):
    if can_take(i, sx, sy):
        queue.append(i)
        visited[i] = 1
    
    if can_take(i, dx, dy):
        end[i] = 1
    
    for j in range(i+1, k):
        if can_transfer(i, j):
            graph[i].append(j)
            graph[j].append(i)

def bfs(queue, visited):
    count = 1
    while queue:
        for _ in range(len(queue)):
            x = queue.popleft()
            
            if end[x]:
                return count
            
            for nx in graph[x]:
                if not visited[nx]:
                    visited[nx] = 1
                    queue.append(nx)
        
        count += 1

answer = bfs(queue, visited)
print(answer)
