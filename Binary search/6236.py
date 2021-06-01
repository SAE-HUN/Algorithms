import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

l = max(arr)
r = l*m

while l<=r:
    mid = (l+r)//2
    cnt = 0
    cash = 0
    
    for i in range(n):
        if cash<arr[i]:
            cnt += 1
            cash = mid
        
        cash -= arr[i]
    
    if cnt>m:
        l = mid+1
    else:
        answer = mid
        r = mid-1

print(answer)
