import sys
input = sys.stdin.readline

n = int(input())
lines = []

for _ in range(n):
    s, e = map(int, input().split())
    lines.append((s, e))

lines.sort(key=lambda x: (x[0], x[1]))
prev_s, prev_e = lines[0][0], lines[0][1]
answer = 0

for s, e in lines:
    if s <= prev_e:
        if e > prev_e:
            prev_e = e
    else:
        answer += prev_e - prev_s
        prev_s, prev_e = s, e

answer += prev_e - prev_s
print(answer)
