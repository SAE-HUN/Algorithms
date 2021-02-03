from collections import deque

r, c = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]

park_cnt = 0
car_cnt = 0

for i in range(r):
    for j in range(c):
        if graph[i][j]=='P':
            graph[i][j] = park_cnt
            park_cnt += 1
        elif graph[i][j]=='C':
            car_cnt += 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, car_num, car_park, time):
    queue = deque([[x, y]])
    visited = [[0]*c for _ in range(r)]
    t = 0
    
    while queue and t<time:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                
                if nx<0 or nx>=r or ny<0 or ny>=c:
                    continue
                
                if not visited[nx][ny] and graph[nx][ny]!='X':
                    visited[nx][ny] = 1
                    queue.append([nx, ny])
                    
                    if type(graph[nx][ny])==int:
                        car_park[car_num].append(graph[nx][ny])
        
        t += 1

def get_available_park(time):
    car_park = [[] for _ in range(car_cnt)]
    car_num = 0
    
    for i in range(r):
        for j in range(c):
            if graph[i][j]=='C':
                bfs(i, j, car_num, car_park, time)
                car_num += 1
    
    return car_park

def dfs(x, c, d, car_park):
    for t in car_park[x]:
        if c[t]:
            continue
        c[t] = True
        if d[t]==-1 or dfs(d[t], c, d, car_park):
            d[t] = x
            return True
    
    return False

def can_all_park(car_park):
    d = [-1]*park_cnt
    
    for i in range(car_cnt):
        c = [0]*park_cnt
        
        if not dfs(i, c, d, car_park):
            return False
    
    return True

left = 0
right = 5000

while left<right:
    m = (left+right)//2
    car_park = get_available_park(m)
    
    if can_all_park(car_park):
        right = m
    else:
        left = m+1

print(-1 if left==5000 else left)
