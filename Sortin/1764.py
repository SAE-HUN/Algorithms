import sys

n, m = map(int, input().split())
names = sys.stdin.read().splitlines()
no_heard = set(names[:n])
no_shown = set(names[n:])

answer = list(no_heard & no_shown)
answer.sort()
print(len(answer))
print('\n'.join(answer))
