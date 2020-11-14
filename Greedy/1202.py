import sys
import heapq
read = lambda: sys.stdin.readline().strip()

n, k = map(int, read().split())

juwelries = []
for i in range(n):
    m, v = map(int, read().split())
    heapq.heappush(juwelries, (m, v))

bags = []
for i in range(k):
    bags.append(int(read()))
bags.sort()

max_heap = []
result = 0
for i in range(k):
    while juwelries and bags[i]>=juwelries[0][0]:
        [m, v] = heapq.heappop(juwelries)
        heapq.heappush(max_heap, -v)
    if max_heap:
        result -= heapq.heappop(max_heap)
    elif not juwelries:
        break
print(result)
