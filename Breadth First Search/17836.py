import heapq

n, m, t = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(n)]

visited = [[[0]*2 for i in range(m)] for _ in range(n)]
visited[0][0][0] = 1
queue = [[1, 0, 0, 0]]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    time, x, y, gram = heapq.heappop(queue)
    gram += (castle[x][y]==2 and not gram)
    visited[x][y][gram] = time
    
    if x==n-1 and y==m-1:
        break
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        
        if not visited[nx][ny][gram]:
            if gram:
                visited[nx][ny][gram] = time+1
                heapq.heappush(queue, [time+1, nx, ny, gram])
            elif castle[nx][ny]!=1:
                visited[nx][ny][gram] = time+1
                heapq.heappush(queue, [time+1, nx, ny, gram])

answer = max(visited[n-1][m-1])
print(answer-1 if answer and answer-1<=t else 'Fail')
