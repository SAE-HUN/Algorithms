s = input().lower()
answer, now = 0, 1

for w in s:
    w = ord(w)-96
    answer += min(abs(w-now), min(now-w+26, w-now+26))
    now = w

print(answer)
