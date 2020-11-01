n, m, k = map(int, input().split())
if n > m*k or n < m+k-1:
    print(-1)
else:
    groups = [0, k]
    n -= k
    m -= 1
    quo = 0 if m==0 else n//m
    rem = 0 if m==0 else n%m
    
    for i in range(m):
        groups.append(groups[-1] + quo + (1 if rem>0 else 0))
        if rem>0: rem-=1
        
    answer = []
    for i in range(1, len(groups)):
        answer.extend(list(range(groups[i], groups[i-1], -1)))
        
    print(' '.join(map(str, answer)))
