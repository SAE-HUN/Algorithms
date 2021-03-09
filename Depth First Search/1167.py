import sys

v = int(input())
graph = [[] for _ in range(v+1)]
weights = [[] for _ in range(v+1)]

for _ in range(v):
    edge = list(map(int, sys.stdin.readline().split()))
    a = edge[0]
    
    for i in range(1, len(edge)-1):
        if i%2:
            graph[a].append(edge[i])
        else:
            weights[a].append(edge[i])

def dfs(x, prev_x):
    first, second = 0, 0
    
    for i in range(len(graph[x])):
        nx = graph[x][i]
        
        if nx==prev_x:
            continue
        
        dist = weights[x][i]+dfs(nx, x)
        
        if dist>=first:
            second = first
            first = dist
        elif dist>second:
            second = dist
    
    cache[x] = [first, second]
    return first

def get_answer(cache):
    answer = 0
    for i in range(1, v+1):
        answer = max(answer, cache[i][0]+cache[i][1])
    
    return answer

cache = [0]*(v+1)
dfs(1, 0)
answer = get_answer(cache)

print(answer)
