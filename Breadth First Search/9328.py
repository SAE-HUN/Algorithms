from collections import deque

def s_int(a):
    return ord(a)-97

def b_int(a):
    return ord(a)-65

t = int(input())
while t:
    h, w = map(int, input().split())
    building = [['.']*(w+2)]
    
    for _ in range(h):
        row = list('.'+input()+'.')
        building.append(row)
    
    building.append(['']*(w+2))
    keys = [0]*26
    ks = input()
    
    if ks!='0':
        for k in ks:
            keys[s_int(k)] = 1
    
    doors = [[] for _ in range(26)]
    queue = deque([[0, 0]])
    visited = [[0]*(w+2) for _ in range(h+2)]
    
    visited[0][0] = 1
    answer = 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx<0 or nx>h+1 or ny<0 or ny>w+1 or visited[nx][ny] or building[nx][ny]=='*':
                continue
            
            n_cell = building[nx][ny]
            
            if 'A'<=n_cell<='Z':
                key = keys[b_int(n_cell)]
                
                if not key:
                    doors[b_int(n_cell)].append([nx, ny])
                    continue
            
            if n_cell=='$':
                answer += 1
            
            if 'a'<=n_cell<='z':
                idx = s_int(n_cell)
                keys[idx] = 1
                queue.extend(doors[idx])
                doors[idx] = []
            
            visited[nx][ny] = 1
            queue.append([nx, ny])
    
    print(answer)
    t -= 1
