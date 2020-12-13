n  = int(input())
arr = sorted([*map(int, input().split())])

i = 0
while i<n-1:
    if arr[i]+1==arr[i+1]:
        j = i+2
        while j<n and arr[i+1]==arr[j]:
            j += 1
        if j==n:
            k = i-1
            while k>-1 and arr[k]==arr[i]:
                k -= 1
            a, b = arr[i], arr[i+1]
            arr[k+1:j] = [b]*(j-i-1) + [a]*(i-k)
        else:
            arr[i+1], arr[j] = arr[j], arr[i+1]
        i = j-1
    i += 1

print(*arr)
