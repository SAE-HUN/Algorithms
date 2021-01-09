from collections import deque

n, k = map(int, input().split())
queue = deque()
answer = [0]*100001

answer[n] = 1
queue.append(n)
d = [(1, 1), (1, -1), (2, 0)]

while queue:
    x = queue.popleft()
    if x==k:
        print(answer[k]-1)
        exit()
    
    for a, b in d:
        nx = a*x+b
        
        if 0<=nx<=100000 and not answer[nx]:
            answer[nx] = answer[x]+1
            queue.append(nx)
