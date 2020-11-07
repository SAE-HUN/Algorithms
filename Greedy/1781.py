import sys
import heapq
input = sys.stdin.readline

n = int(input().strip())
questions = [tuple(map(int, input().split())) for _ in range(n)]
questions.sort(key=lambda x:(x[0], -x[1]))

cup_ramens = []
for deadline, cup_ramen in questions:
    heapq.heappush(cup_ramens, cup_ramen)
    
    if len(cup_ramens) > deadline:
        heapq.heappop(cup_ramens)
        
print(sum(cup_ramens))
