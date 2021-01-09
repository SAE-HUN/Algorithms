n = int(input())
town = [list(map(int, input().strip())) for _ in range(n)]

def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    count = 0
    stack = [(x, y)]
    town[x][y] = 0
    
    while stack:
        x, y = stack.pop()
        count += 1
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            
            if town[nx][ny]:
                stack.append((nx, ny))
                town[nx][ny] = 0
    
    return count

answer = [0]
for i in range(n):
    for j in range(n):
        if town[i][j]:
            answer[0] += 1
            answer.append(dfs(i, j))

print(answer[0])
for a in sorted(answer[1:]):
    print(a)
