import sys

n = int(input())
total, towns = 0, []

for _ in range(n):
    loc, mnt = map(int, sys.stdin.readline().split())
    total+=mnt; towns.append((loc, mnt))

stack = 0; towns.sort()

for loc, mnt in towns:
    stack += mnt
    if stack>=total/2:
        print(loc)
        break
