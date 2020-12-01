n = int(input())
max_start, min_end = 0, 100000

for _ in range(n):
    s, e = map(int, input().split())
    max_start = max(max_start, s)
    min_end = min(min_end, e)

print(max_start-min_end if max_start-min_end>0 else 0)
