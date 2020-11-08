import heapq

n = int(input())
lectures = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x:x[1])
ps = []

for p, d in lectures:
    heapq.heappush(ps, p)
    
    if len(ps)>d:
        heapq.heappop(ps)

print(sum(ps))
