import copy
import collections

def right(board):
    for i in range(n):
        prev = [0, [0, 0]]
        for j in range(n-1, -1, -1):
            if board[i][j]:
                if board[i][j]==prev[0]:
                    board[prev[1][0]][prev[1][1]] *= 2
                    board[i][j] = 0
                    prev = [0, [0, 0]]
                else:
                    prev = [board[i][j], [i, j]]
        
        no_zeros = collections.deque()
        for j in range(n-1, -1, -1):
            if board[i][j]:
                no_zeros.append(board[i][j])
        
        for j in range(n-1, -1, -1):
            if no_zeros:
                board[i][j] = no_zeros.popleft()
            else:
                board[i][j] = 0

def left(board):
    for i in range(n):
        prev = [0, [0, 0]]
        for j in range(n):
            if board[i][j]:
                if board[i][j]==prev[0]:
                    board[prev[1][0]][prev[1][1]] *= 2
                    board[i][j] = 0
                    prev = [0, [0, 0]]
                else:
                    prev = [board[i][j], [i, j]]
        
        no_zeros = collections.deque()
        for j in range(n):
            if board[i][j]:
                no_zeros.append(board[i][j])
        
        for j in range(n):
            if no_zeros:
                board[i][j] = no_zeros.popleft()
            else:
                board[i][j] = 0

def up(board):
    for i in range(n):
        prev = [0, [0, 0]]
        for j in range(n):
            if board[j][i]:
                if board[j][i]==prev[0]:
                    board[prev[1][0]][prev[1][1]] *= 2
                    board[j][i] = 0
                    prev = [0, [0, 0]]
                else:
                    prev = [board[j][i], [j, i]]
        
        no_zeros = collections.deque()
        for j in range(n):
            if board[j][i]:
                no_zeros.append(board[j][i])
        
        for j in range(n):
            if no_zeros:
                board[j][i] = no_zeros.popleft()
            else:
                board[j][i] = 0

def down(board):
    for i in range(n):
        prev = [0, [0, 0]]
        for j in range(n-1, -1, -1):
            if board[j][i]:
                if board[j][i]==prev[0]:
                    board[prev[1][0]][prev[1][1]] *= 2
                    board[j][i] = 0
                    prev = [0, [0, 0]]
                else:
                    prev = [board[j][i], [j, i]]
        
        no_zeros = collections.deque()
        for j in range(n-1, -1, -1):
            if board[j][i]:
                no_zeros.append(board[j][i])
        
        for j in range(n-1, -1, -1):
            if no_zeros:
                board[j][i] = no_zeros.popleft()
            else:
                board[j][i] = 0

def get_max(board):
    max_num = 0
    
    for i in range(n):
        for j in range(n):
            max_num = max(max_num, board[i][j])
    
    return max_num

def dfs(direction, board, move):
    move += 1
    
    if direction==0:right(board)
    elif direction==1:left(board)
    elif direction==2:up(board)
    else:down(board)
    
    if move==5:
        max_num = get_max(board)
        max_nums.append(max_num)
        return
    
    for i in range(4):
        dfs(i, copy.deepcopy(board), move)

n = int(input())
board = [[*map(int, input().split())] for _ in range(n)]

max_nums = []

for i in range(4):
    dfs(direction=i, board=copy.deepcopy(board), move=0)

print(max(max_nums))
