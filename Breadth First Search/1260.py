import heapq
from collections import deque 
import copy

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)] 

def dfs(x, graph, visit):
    visit[x] = True
    print(x, end=' ')
    
    for _ in range(len(graph[x])):
        y = heapq.heappop(graph[x])
        if not visit[y]:
            dfs(y, graph, visit)

def bfs(graph):
    visit = [False]*(n+1)
    queue = deque([v])
    visit[v] = True
    
    while queue:
        x = queue.popleft()
        print(x, end=' ')
        
        for _ in range(len(graph[x])):
            y = heapq.heappop(graph[x])
            if not visit[y]:
                visit[y] = True
                queue.append(y) 

for _ in range(m):
    a, b = map(int, input().split())
    heapq.heappush(graph[a], b)
    heapq.heappush(graph[b], a) 

dfs(v, copy.deepcopy(graph), [False]*(n+1))
print()
bfs(copy.deepcopy(graph))
