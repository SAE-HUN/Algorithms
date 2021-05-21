from bisect import bisect_left, bisect_right

import sys
input = sys.stdin.readline

def MIS():
    return map(int, input().split())

n, s, p = MIS()
rank = [*MIS()]
rank.reverse()

if n<p:
    i = bisect_right(rank, s)
    print(n-i+1)
else:
    if rank[0]>=s:
        print(-1)
    else:
        i = bisect_right(rank, s)
        print(n-i+1)
