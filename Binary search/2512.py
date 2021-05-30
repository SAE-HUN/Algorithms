n = int(input())
arr = list(map(int, input().split()))
m = int(input())

start = 0
end = max(arr)

while start<=end:
    mid = (start+end)//2
    tmp = 0
    
    for i in range(n):
        tmp += min(arr[i], mid)
    
    if tmp>m:
        end = mid-1
    else:
        answer = mid
        start = mid+1

print(answer)
