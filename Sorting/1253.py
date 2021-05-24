import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = 0

for i in range(n):
    l = 0
    r = n-1
    
    while l<r:
        s = arr[l]+arr[r]
        
        if s==arr[i]:
            if l!=i and r!=i:
                answer += 1
                break
            elif l==i:
                l += 1
            elif r==i:
                r -= 1
        elif s<arr[i]:
            l += 1
        else:
            r -= 1

print(answer)
