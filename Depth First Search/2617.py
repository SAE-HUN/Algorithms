n, m = map(int, input().split())
v = [[] for _ in range(n+1)]
r = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    v[a].append(b)
    r[b].append(a)

def dfs(x):
    global cnt
    
    for nx in v[x]:
        if not visited[nx]:
            visited[nx] = 1
            dfs(nx)
            cnt += 1

def r_dfs(x):
    global r_cnt
    
    for nx in r[x]:
        if not r_visited[nx]:
            r_visited[nx] = 1
            r_dfs(nx)
            r_cnt += 1

answer = 0
for i in range(n):
    cnt = 0
    r_cnt = 0
    
    visited = [0]*(n+1)
    r_visited = [0]*(n+1)
    
    dfs(i+1)
    r_dfs(i+1)
    
    if cnt>n//2 or r_cnt>n//2:
        answer += 1

print(answer)
