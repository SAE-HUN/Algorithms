import heapq

n = int(input())
stations = [(0, 0)]

for _ in range(n):
    a, b = map(int, input().split())
    stations.append((a, b))

l, p = map(int, input().split())
stations.append((l, 0))
stations.sort()
answer, now, fuels = 0, p, []

for i in range(1, n+2):
    s = stations[i]
    loc, fuel = s[0], s[1]
    now -= loc - stations[i-1][0]
    
    if now >= 0:
        heapq.heappush(fuels, -fuel)
        continue
    
    if not fuels:
        print(-1)
        exit()
    
    while True:
        now -= heapq.heappop(fuels)
        answer += 1
        
        if now >= 0:
            heapq.heappush(fuels, -fuel)
            break
        
        if not fuels:
            print(-1)
            exit()

print(answer)
