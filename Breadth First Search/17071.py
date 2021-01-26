from collections import deque

def MIS():
    return map(int, input().split())

n, k = MIS()

if n==k:
    print(0)
    exit()

visited = [[0]*2 for _ in range(500001)]
visited[n][0] = 1
queue = deque([[n, 0]])

while queue:
    x, t = queue.popleft()
    
    for a, b in [(2, 0), (1, -1), (1, 1)]:
        nx = a*x+b
        
        if nx<0 or nx>500000:
            continue
        
        if not visited[nx][(t+1)%2]:
            visited[nx][(t+1)%2] = t+1
            queue.append([nx, t+1])

answer = 0
while k<=500000:
    if 0<visited[k][answer%2]<=answer:
        print(answer)
        exit()
    
    answer += 1
    k += answer

print(-1)
