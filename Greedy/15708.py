import sys
import heapq

def II():
    return int(sys.stdin.readline().strip())

def MIS():
    return map(int, sys.stdin.readline().split())

n, t, p = MIS()
arr = [*MIS()]

_sum, answer = 0, 0
pq = []

for i, k in enumerate(arr):
    _sum += k
    heapq.heappush(pq, -k)
    
    while pq and _sum>t-i*p:
        _sum += heapq.heappop(pq)
    
    answer = max(answer, len(pq))

print(answer)
