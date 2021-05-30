x, y = map(int, input().split())
z = int(100*y/x)
l = 0
r = x

if z==100 or z==99:
    print(-1)
    exit()

while l<=r:
    m = (l+r)//2
    _z = int(100*(y+m)/(x+m))
    
    if _z<=z:
        l = m+1
    else:
        answer = m
        r = m-1

print(answer)
