from collections import deque

def MIS():
    return map(int, input().split())

n, k, m = MIS()
graph = [[] for _ in range(n+1)]
tubes = []

for i in range(m):
    hyper = list(MIS())
    tubes.append(hyper)
    
    for s in hyper:
        graph[s].append(i)

cache = [0]*(n+1)
visited = [0]*m
cache[1] = 1
queue = deque([1])

while queue:
    x = queue.popleft()
    
    if x==n:
        print(cache[n])
        exit()
    
    for n_tube in graph[x]:
        if visited[n_tube]:
            continue
        
        for nx in tubes[n_tube]:
            if cache[nx]:
                continue
            cache[nx] = cache[x]+1
            queue.append(nx)
        
        visited[n_tube] = 1

print(-1)
