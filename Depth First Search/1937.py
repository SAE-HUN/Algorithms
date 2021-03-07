import sys
sys.setrecursionlimit(1000000)

n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]
cache = [[0]*n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if not cache[x][y]:
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            
            if forest[nx][ny]>forest[x][y]:
                cache[x][y] = max(cache[x][y], dfs(nx, ny))
        
        cache[x][y] += 1
    
    return cache[x][y]

for i in range(n):
    for j in range(n):
        if not cache[i][j]:
            dfs(i, j)

answer = 0
for row in cache:
    answer = max(answer, max(row))

print(answer)
