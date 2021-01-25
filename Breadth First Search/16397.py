from collections import deque

def MIS():
    return map(int, input().split())

n, t, g = MIS()
cache = [0]*100000
cache[n] = 1
queue = deque([n])

while queue:
    x = queue.popleft()
    
    if cache[x]-1>t:
        print('ANG')
        exit()
    
    if x==g:
        print(cache[x]-1)
        exit()
    
    if x+1<=99999 and not cache[x+1]:
        cache[x+1] = cache[x]+1
        queue.append(x+1)
    
    if 0<2*x<=99999:
        nx = 2*x
        nx -= 10**(len(str(nx))-1)
        
        if not cache[nx]:
            cache[nx] = cache[x]+1
            queue.append(nx)

print('ANG')
