import bisect
import sys

n = int(input())
total, towns = 0, []

for _ in range(n):
    loc, mnt = map(int, sys.stdin.readline().split())
    total+=mnt; towns.append([loc, mnt])

stack = 0; towns.sort()

for i, (loc, mnt) in enumerate(towns):
    stack += mnt
    towns[i][1] = stack

print(towns[bisect.bisect_left([*map(lambda x:x[1], towns)], total/2)][0])
