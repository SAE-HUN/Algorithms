import copy
import sys

sys.setrecursionlimit(10 ** 6)

def get_safe_zone(rain, area):
    for i in range(n):
        for j in range(n):
            if area[i][j]<=rain:
                area[i][j] = 0
            else:
                area[i][j] = 1
    
    return area

def dfs(x, y, zone):
    zone[x][y] = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if -1<nx<n and -1<ny<n and zone[nx][ny]:
            dfs(nx, ny, zone)
    
    return

def get_safe_cnt(zone):
    cnt = 0
    
    for i in range(n):
        for j in range(n):
            if zone[i][j]:
                dfs(i, j, zone)
                cnt += 1
    
    return cnt

n = int(input())
area = [[*map(int, input().split())] for _ in range(n)]
answer = 0

for rain in range(101):
    safe_zone = get_safe_zone(rain, copy.deepcopy(area))
    safe_cnt = get_safe_cnt(safe_zone)
    answer = max(answer, safe_cnt)

print(answer)
