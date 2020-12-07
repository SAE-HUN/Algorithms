import copy

def dfs(x, y, total, visited):
    total += paper[x][y]
    visited.append((x, y))
    
    if len(visited)==4:
        totals.append(total)
        return
        
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if -1<nx<n and -1<ny<m and not (nx, ny) in visited:
            dfs(nx, ny, total, visited)
            visited.pop()

def fuck(x, y):
    ds = [
        [(0, 1), (0, 2), (-1, 1)], [(1, 0), (2, 0), (1, 1)],
        [(0, 1), (0, 2), (1, 1)], [(1, 0), (2, 0), (1, -1)]
    ]
    
    
    for d in ds:
        total = paper[x][y]
        visited = [(x, y)]
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if -1<nx<n and -1<ny<m:
                visited.append((nx, ny))
                total += paper[nx][ny]
            else:
                break
        
        if len(visited)==4:
            totals.append(total)

n, m = map(int, input().split())
paper = [[*map(int, input().split())] for _ in range(n)]
totals, dx, dy = [], [0, 1, 0, -1], [1, 0, -1, 0]

for i in range(n):
    for j in range(m):
        dfs(i, j, 0, [])
        fuck(i, j)

print(max(totals))
