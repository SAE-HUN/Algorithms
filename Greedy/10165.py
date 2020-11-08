import sys

n = int(input())
m = int(input())

routes = []
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if a>b:
        b += n
    routes.append((a, b, i+1))
    
routes.sort(key=lambda x:(x[0], -x[1]))
max_b = routes[0][1]
cancelled = []

for i in range(1, m):
    a, b, num = routes[i]
    if b <= max_b:
        cancelled.append(num)
        continue
    max_b = b

if max_b >= n:
    max_b -= n

    for i in range(m):
        a, b, num = routes[i]
        if a >= max_b:
            break
        if b <= max_b:
            cancelled.append(num)

answer = sorted(set(range(1, m+1)).difference(set(cancelled)))
print(' '.join(map(str, answer)))
