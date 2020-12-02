import sys
n, ss = int(input()), sys.stdin.read().split()
no_zero, scores = [], {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0}

for s in ss:
    no_zero.append(s[0])
    for i, alp in enumerate(s):
        scores[alp] += 10**(len(s)-i)

match, no_zero = {}, list(set(no_zero))
scores = list(scores.items()); scores.sort(key=lambda x:x[1])

for i, (alp, score) in enumerate(scores):
    if alp not in no_zero:
        match[scores.pop(i)[0]] = '0'
        break

_next = 1
for alp, score in scores:
    match[alp] = str(_next)
    _next += 1

answer = 0
for s in ss:
    temp = ''
    for alp in s:
        temp += match[alp]
    answer += int(temp)

print(answer)
