from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start, end):
    if not start<= arr[0][0]<=end:
        return False
    
    visited = [[0]*n for _ in range(n)]
    queue = deque([[0, 0]])
    
    while queue:
        x, y = queue.popleft()
        
        if x==n-1 and y==n-1:
            return True
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            
            if not visited[nx][ny] and start<=arr[nx][ny]<=end:
                visited[nx][ny] = 1
                queue.append([nx, ny])
    
    return False

end = 0 
answer = 200

for start in range(201):
    while end<=200:
        if bfs(start, end):
            answer = min(answer, end-start)
            break
        else:
            end += 1

print(answer)
