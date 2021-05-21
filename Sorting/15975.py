import sys
input = sys.stdin.readline

n = int(input())
arr = [[*map(int, input().split())] for _ in range(n)]
arr.sort(key=lambda x:(x[1], x[0]))
answer = 0

for i in range(n):
    if i==0:
        if arr[i+1][1]==arr[i][1]:
            answer += arr[i+1][0] - arr[i][0]
    elif i==n-1:
        if arr[i-1][1]==arr[i][1]:
            answer += arr[i][0] - arr[i-1][0]
    else:
        if arr[i+1][1]==arr[i][1] and arr[i-1][1]==arr[i][1]:
            answer += min(arr[i+1][0] - arr[i][0],arr[i][0] - arr[i-1][0])
        elif arr[i+1][1]==arr[i][1]:
            answer += arr[i+1][0] - arr[i][0]
        elif arr[i-1][1]==arr[i][1]:
            answer += arr[i][0] - arr[i-1][0]

print(answer)
