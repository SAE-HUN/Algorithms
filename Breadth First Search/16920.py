from collections import deque

n, m, p = map(int, input().split())
s = list(map(int, input().split()))
graph = [list(input().strip()) for _ in range(n)]
castle = [deque() for _ in range(p)]

for i in range(n):
    for j in range(m):
        if graph[i][j]=='.':
            graph[i][j] = 0
        elif graph[i][j]=='#':
            graph[i][j] = -1
        else:
            graph[i][j] = int(graph[i][j])
            castle[graph[i][j]-1].append([i, j])

end = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a):
    if not castle[a]:
        return
    
    global end
    t = 0
    
    while castle[a] and t<s[a]:
        for _ in range(len(castle[a])):
            x, y = castle[a].popleft()
            
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                
                if nx<0 or nx>=n or ny<0 or ny>=m:
                    continue
                
                if not graph[nx][ny]:
                    graph[nx][ny] = a+1
                    castle[a].append([nx, ny])
        
        t += 1
    
    if not castle[a]:
        end += 1

while end<p:
    for i in range(p):
        bfs(i)

answer = [0]*p
for i in range(n):
    for j in range(m):
        a = graph[i][j]
        if a>0:
            answer[a-1] += 1

print(*answer)
