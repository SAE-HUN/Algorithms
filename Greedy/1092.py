import bisect
import sys
import collections

n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

_cranes = sorted(list(set(cranes)))
box_cnt = [0] * len(_cranes)

for box in boxes:
  idx = bisect.bisect_left(_cranes, box)
  if idx == len(_cranes):
    print(-1)
    sys.exit()
  box_cnt[idx] += 1
  
crane_cnt = [x[1] for x in sorted(collections.Counter(cranes).items())]
answer = 0

while m>0:
  for i in range(len(_cranes)-1, 0, -1):
    if box_cnt[i] == 0:
      crane_cnt[i-1] += crane_cnt[i]
      crane_cnt[i] = 0
    if box_cnt[i] >= crane_cnt[i]:
      box_cnt[i] -= crane_cnt[i]
      m -= crane_cnt[i]
    else:
      crane_cnt[i-1] += crane_cnt[i] - box_cnt[i]
      crane_cnt[i] = box_cnt[i]
      m -= box_cnt[i]
      box_cnt[i] = 0
  if box_cnt[0]:
    if box_cnt[0] >= crane_cnt[0]:
      box_cnt[0] -= crane_cnt[0]
      m -= crane_cnt[0]
    else:
      m -= box_cnt[0]
      box_cnt[0] = 0
  
  answer += 1

print(answer)
