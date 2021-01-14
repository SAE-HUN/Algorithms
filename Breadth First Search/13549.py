import heapq

n, k = map(int, input().split())
visited = [0]*100001
visited[n] = 1
queue = [[0, n]]

a = [2, 1, 1]
b = [0, 1, -1]

while queue:
    time, x = heapq.heappop(queue)
    
    if x==k:
        print(time)
        exit()
    
    for i in range(3):
        nx = a[i]*x+b[i]
        
        if nx<0 or nx>100000:
            continue
        
        if not visited[nx]:
            visited[nx] = 1
            heapq.heappush(queue, [time+bool(i), nx])
