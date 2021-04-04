import sys

sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

cache = [[0]*m for _ in range(n)]
visited = [[0]*m for _ in range(n)]

def get_n(x, y):
    d = board[x][y]
    if d=='U':
        return x-1, y
    elif d=='D':
        return x+1, y
    elif d=='L':
        return x, y-1
    else:
        return x, y+1

def dfs(x, y):
    nx, ny = get_n(x, y)
    
    if nx<0 or nx>=n or ny<0 or ny>=m or cache[nx][ny]==1:
        cache[x][y] = 1
        return cache[x][y]
    
    if cache[nx][ny]==-1 or visited[nx][ny]:
        cache[x][y] = -1
    
    if not cache[nx][ny] and not visited[nx][ny]:
        visited[nx][ny] = 1
        cache[x][y] = dfs(nx, ny)
        visited[nx][ny] = 0
    
    return cache[x][y]

for i in range(n):
    for j in range(m):
        if not cache[i][j]:
            visited[i][j] = 1
            dfs(i, j)
            visited[i][j] = 0

answer = 0
for i in range(n):
    for j in range(m):
        if cache[i][j]==1:
            answer += 1

print(answer)
