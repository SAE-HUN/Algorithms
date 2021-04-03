import sys

sys.setrecursionlimit(10**6)

n = int(input())
island = [0, 0]
tree = [[] for _ in range(n+1)]

for i in range(2, n+1):
    t, a, p = sys.stdin.readline().split()
    tree[int(p)].append(i)
    island.append(int(a)*(2*(t=='S')-1))

def dfs(x):
    for nx in tree[x]:
        island[x] += dfs(nx)
    
    return island[x]*(island[x]>0)

dfs(1)
print(island[1])
