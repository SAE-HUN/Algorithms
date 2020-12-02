import sys

n = int(input())
scores = [*map(int, sys.stdin.read().split())]
scores.sort()

answer, _next = 0, 1
for score in scores:
    if score>=_next:
        answer += score - _next
        _next += 1

print(answer)
