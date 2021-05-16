import sys
from collections import Counter

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.read().rstrip().split('\n')))

s = sum(arr)
if s/n - s//n >= 0.5:
    mean = s//n + 1
else:
    mean = s//n

arr.sort()
median = arr[n//2]
_range = arr[-1] - arr[0]
mode = Counter(arr).most_common(2)

if len(mode) == 2 and mode[0][1] == mode[1][1]:
    mode = mode[1][0]
else:
    mode = mode[0][0]

print(mean)
print(median)
print(mode)
print(_range)
