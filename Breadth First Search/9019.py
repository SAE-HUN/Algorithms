from collections import deque

d = ['D', 'S', 'L', 'R']

def bfs(a, b):
    cache = [0]*10000
    cache[a] = ' '
    queue = deque([a])
    
    while queue:
        x = queue.popleft()
        
        for i in range(4):
            nx = cal(x, i)
            
            if nx==b:
                return cache[x]+d[i]
            
            if not cache[nx]:
                cache[nx] = cache[x]+d[i]
                queue.append(nx)

def cal(x, i):
    if i==0:
        return 2*x%10000
    if i==1:
        return x-1+10000*(not x)
    if i==2:
        return x%1000*10+x//1000
    if i==3:
        return x%10*1000+x//10

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(bfs(a, b).strip())
