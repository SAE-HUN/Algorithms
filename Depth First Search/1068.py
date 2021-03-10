n = int(input())
graph = list(map(int ,input().split()))
a = int(input())

if graph[a]==-1:
    print(0)
    exit()

_graph = [[] for _ in range(n)]
for i in range(n):
    if graph[i]==-1:
        continue
    
    _graph[graph[i]].append(i)

check = [0]*n
for i in range(n):
    if graph[i]==-1:
        continue
    check[graph[i]] = 1

def dfs(x):
    check[x] = 1
    for nx in _graph[x]:
        dfs(nx)

dfs(a)
answer = 0
if len(_graph[graph[a]])==1:
    answer += 1

for i in range(n):
    if not check[i]:
        answer += 1

print(answer)
