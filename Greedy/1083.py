n = int(input())
arr = list(map(int, input().split()))
s = int(input())
answer = []

while s and arr:
    num, idx = 0, None
    for i in range(len(arr)):
        if i>s:
            break
        if arr[i]>num:
            num = arr[i]
            idx = i
    
    s -= idx
    answer.append(arr.pop(idx))

answer.extend(arr)
print(*answer)
