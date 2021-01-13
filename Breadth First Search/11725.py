from collections import deque
import sys

n = int(input())
graph = [[] for _ in range(n+1)]
cache = [0]*(n+1)

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([1])
while queue:
    x = queue.popleft()
    
    for nx in graph[x]:
        if not cache[nx]:
            cache[nx] = x
            queue.append(nx)

for i in range(2, n+1):
    print(cache[i])
