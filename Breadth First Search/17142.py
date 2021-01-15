from itertools import combinations
from collections import deque

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

def bfs(virus):
    queue = deque(virus)
    cache = [[0]*n for _ in range(n)]
    
    for x, y in virus:
        cache[x][y] = 1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            
            if not cache[nx][ny] and lab[nx][ny]!=1:
                cache[nx][ny] = cache[x][y]+1
                queue.append([nx, ny])
    
    return cache

def get_result(cache):
    result = 1
    for i in range(n):
        for j in range(n):
            if not cache[i][j] and lab[i][j]!=1:
                return False
            
            if lab[i][j]==1 or lab[i][j]==2:
                continue
            
            result = max(result, cache[i][j])
    
    return result

viruses = []
for i in range(n):
    for j in range(n):
        if lab[i][j]==2:
            viruses.append([i, j])

answer = 10000
virus_combi = combinations(viruses, m)
for virus in virus_combi:
    cache = bfs(virus)
    result = get_result(cache)
    
    if result:
        answer = min(answer, result-1)

print(answer if answer!=10000 else -1)
