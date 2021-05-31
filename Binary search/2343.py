n, m = map(int, input().split())
lessons = list(map(int, input().split()))
a = min(lessons)

l = 0
r = 10**4 * 10**5

while l<=r:
    mid = (l+r)//2
    cnt = 1
    tmp = 0
    
    for i in range(n):
        if lessons[i]>mid:
            cnt = m+1
            break
        
        if tmp+lessons[i]>mid:
            tmp = lessons[i]
            cnt += 1
            continue
        
        tmp += lessons[i]
    
    if cnt>m:
        l = mid+1
    else:
        answer = mid
        r = mid-1

print(answer)
