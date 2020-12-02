from heapq import *
import sys

input, t = sys.stdin.readline, int(input())

for _ in range(t):
    n = int(input())
    slimes = [*map(int, input().split())]
    answer = 1; heapify(slimes)
    
    while len(slimes)>1:
        a, b = heappop(slimes), heappop(slimes)
        c = a*b; answer *= c; heappush(slimes, c)
    
    print(answer%1000000007)
