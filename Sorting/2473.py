n = int(input())
arr = sorted(map(int, input().split()))
arr.sort()

answer = None
s = float('inf')

for i in range(n-2):
    l = i+1
    r = n-1
    
    while l<r:
        tmp = arr[i] + arr[l] + arr[r]
        
        if abs(tmp)<s:
            answer = [arr[i], arr[l], arr[r]]
            s = abs(tmp)
        
        if tmp<0:
            l += 1
        elif tmp>0:
            r -= 1
        else:
            print(arr[i], arr[l], arr[r])
            exit()


print(*answer)
