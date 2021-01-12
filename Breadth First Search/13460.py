from collections import deque

n, m = map(int, input().split())

board = []
for i in range(n):
    row = list(input())
    board.append(row)
    
    for j, cell in enumerate(row):
        if cell=='B':
            blue = (i, j)
        elif cell=='R':
            red = (i, j)
        elif cell=='O':
            hole = (i, j)

def move(nx, ny, dx, dy):
    count = 0
    while board[nx+dx][ny+dy]!='#' and board[nx][ny]!='O':
        nx += dx
        ny += dy
        count += 1
    
    return [nx, ny], count

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[[[False]*m for k in range(n)] for j in range(m)] for i in range(n)]
visited[red[0]][red[1]][blue[0]][blue[1]] = True

queue = deque()
queue.append((red, blue, 0))
while queue:
    red, blue, count = queue.popleft()
    
    if count>=10:
        continue
    
    for i in range(4):
        n_red, r_count = move(red[0], red[1], dx[i], dy[i])
        
        n_blue, b_count = move(blue[0], blue[1], dx[i], dy[i])
        
        if board[n_blue[0]][n_blue[1]]=='O':
            continue
        
        if board[n_red[0]][n_red[1]]=='O':
            print(count+1)
            exit()
        
        if n_red==n_blue:
            n_red[0] -= dx[i]*(r_count>b_count)
            n_red[1] -= dy[i]*(r_count>b_count)
            n_blue[0] -= dx[i]*(b_count>r_count)
            n_blue[1] -= dy[i]*(b_count>r_count)
        
        if not visited[n_red[0]][n_red[1]][n_blue[0]][n_blue[1]]:
            visited[n_red[0]][n_red[1]][n_blue[0]][n_blue[1]] = True
            queue.append((n_red, n_blue, count+1))

print(-1)
