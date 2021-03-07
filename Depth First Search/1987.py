r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]

answer = 0
alphabet = [0]*26

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, cnt):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if nx<0 or nx>=r or ny<0 or ny>=c:
            continue
        
        if not alphabet[ord(board[nx][ny])-65]:
            alphabet[ord(board[nx][ny])-65] = 1
            dfs(nx, ny, cnt+1)
            alphabet[ord(board[nx][ny])-65] = 0
        else:
            global answer
            answer = max(answer, cnt)

alphabet[ord(board[0][0])-65] = 1
dfs(0, 0, 1)

print(answer)
