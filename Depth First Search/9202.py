import sys

w = int(input())
words = set()
for _ in range(w):
    word = sys.stdin.readline().strip()
    words.add(word)

dx = [-1, -1, -1, 1, 1, 1, 0, 0]
dy = [-1, 0, 1, -1, 0, 1, -1, 1]
score = [0, 0, 0, 1, 1, 2, 3, 5, 11]

def dfs(x, y, depth):
    global word
    global visited
    
    _word = ''.join(word)
    if _word in words:
        answer.add(_word)
    
    if depth==8:
        return
    
    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if nx<0 or nx>3 or ny<0 or ny>3:
            continue
        
        if not visited[nx][ny]:
            visited[nx][ny] = 1
            word.append(boggle[nx][ny])
            dfs(nx, ny, depth+1)
            word.pop()
            visited[nx][ny] = 0

input()
b = int(input())
visited = [[0]*4 for _ in range(4)]

while b:
    b -= 1
    boggle = []
    
    for _ in range(4):
        row = list(input().strip())
        boggle.append(row)
    
    answer = set()
    for i in range(4):
        for j in range(4):
            word = [boggle[i][j]]
            visited[i][j] = 1
            dfs(i, j, 1)
            visited[i][j] = 0
    
    point = 0
    answer = list(answer)
    answer.sort(key=lambda x:(-len(x), x), reverse=True)
    
    for word in answer:
        point += score[len(word)]
    
    print(point, answer[-1], len(answer))
    try:
        input()
    except:
        pass
