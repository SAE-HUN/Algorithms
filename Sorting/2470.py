n = int(input())
arr = list(map(int, input().split()))
arr.sort()

l = 0
r = n-1
answer = [10**9, 10**9]

while l<r:
    tmp = arr[l]+arr[r]
    
    if abs(tmp)<abs(answer[0]+answer[1]):
        answer = [arr[l], arr[r]]
    
    if tmp>0:
        r -= 1
    elif tmp<0:
        l += 1
    else:
        print(arr[l], arr[r])
        exit()

print(*answer)
