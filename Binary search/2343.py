n, m = map(int, input().split())
lessons = list(map(int, input().split()))
a = max(lessons)

l = 0
r = 10**4 * 10**5

while l<=r:
    mid = (l+r)//2
    cnt = 1
    tmp = 0
    
    if mid<a:
        l = mid+1
        continue
    
    for i in range(n):
        if tmp+lessons[i]>mid:
            tmp = 0
            cnt += 1
        
        tmp += lessons[i]
    
    if cnt>m:
        l = mid+1
    else:
        answer = mid
        r = mid-1

print(answer)
