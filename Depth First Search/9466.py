t = int(input())

def mark(a, queue):
    global cache
    b = -1
    
    for c in queue:
        if c==a:
            b = 1
        
        cache[c] = b

def dfs(x):
    visited = set([x])
    queue = [x]
    
    while queue:
        x = queue[-1]
        nx = graph[x]-1
        
        if cache[nx]:
            mark(0, queue)
            return
        elif nx in visited:
            mark(nx, queue)
            return
        else:
            queue.append(nx)
            visited.add(nx)

while t:
    t -= 1
    n = int(input())
    graph = list(map(int, input().split()))
    cache = [0]*n
    
    for i in range(n):
        if not cache[i]:
            dfs(i)
    
    answer = 0
    for i in range(n):
        if cache[i]==-1:
            answer += 1
    
    print(answer)
