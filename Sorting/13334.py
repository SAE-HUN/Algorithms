import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    h, o = map(int, input().split())
    if h>o:
        h, o = o, h
    arr.append([h, o])

d = int(input())
arr.sort(key=lambda x:(x[1], x[0]))
heap = []
answer = 0

for i in range(n):
    l, r = arr[i]
    heapq.heappush(heap, l)
    
    while heap and r-d>heap[0]:
        heapq.heappop(heap)
    
    answer = max(answer, len(heap))

print(answer)
