from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

order = list(map(int, input().split()))

if order[0]!=1:
    print(0)
    exit()

visited = [0]*(n+1)
visited[1] = 1
queue = deque([1])
prev_idx = 1

while queue:
    for _ in range(len(queue)):
        tmp_q = []
        x = queue.popleft()
        
        for nx in graph[x]:
            if not visited[nx]:
                visited[nx] = 1
                tmp_q.append(nx)
        
        next_idx = prev_idx+len(tmp_q)
        tmp_ord = order[prev_idx:next_idx]
        prev_idx = next_idx
        
        if set(tmp_q)-set(tmp_ord):
            print(0)
            exit()
        else:
            queue.extend(tmp_ord)

print(1)
