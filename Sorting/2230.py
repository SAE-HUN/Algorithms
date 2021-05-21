from bisect import bisect_left
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
answer = float('inf')

for i in range(n):
    j = bisect_left(arr, arr[i]+m)
    if j<n:
        answer = min(answer, arr[j]-arr[i])

print(answer)
