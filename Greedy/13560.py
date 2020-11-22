import heapq

n = int(input())
scores = list(map(lambda x:-int(x), input().split()))
heapq.heapify(scores)

for i in range(n):
    score = -heapq.heappop(scores)
    num = n-score-i-1
    
    if num<0 or score<0:
        print(-1)
        exit()
    
    for j in range(num):
        a = -heapq.heappop(scores)
        a -= 1
        heapq.heappush(scores, -a)

print(1)
