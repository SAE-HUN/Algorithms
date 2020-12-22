import sys
import heapq

def II():
    return int(sys.stdin.readline().strip())

def MIS():
    return map(int, sys.stdin.readline().split())

n = II()
mman, pman = [], []
mwoman, pwoman = [], []

for tall in MIS():
    if tall>0:
        heapq.heappush(pman, tall)
    else:
        heapq.heappush(mman, -tall)

for tall in MIS():
    if tall>0:
        heapq.heappush(pwoman, tall)
    else:
        heapq.heappush(mwoman, -tall)

answer = 0

while pman and mwoman:
    man = heapq.heappop(pman)
    while mwoman:
        woman = heapq.heappop(mwoman)
        if woman>man:
            answer += 1
            break

while pwoman and mman:
    woman = heapq.heappop(pwoman)
    while mman:
        man = heapq.heappop(mman)
        if man>woman:
            answer += 1
            break

print(answer)
