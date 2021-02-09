from collections import deque

n, t = map(int, input().split())
graph = [set() for _ in range(1000001)]

for _ in range(n):
    x, y = map(int, input().split())
    graph[x].add(y)

queue = deque([[0, 0]])
answer = 0

while queue:
    for _ in range(len(queue)):
        x, y = queue.popleft()
        
        if y==t:
            print(answer)
            exit()
        
        for i in range(-2, 3):
            for j in range(-2, 3):
                nx = x+i
                ny = y+j
                
                if nx<0 or nx>1000000 or ny<0 or ny>t:
                    continue
                
                try:
                    graph[nx].remove(ny)
                    queue.append([nx, ny])
                except:
                    pass
    
    answer += 1

print(-1)
