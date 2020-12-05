import sys
input = sys.stdin.readline

c, n = map(int, input().split())
chickens = sorted([[int(input()), True] for _ in range(c)])
cows = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x:(x[1], x[0]))

answer = 0
for a, b in cows:
    for i, (t, check) in enumerate(chickens):
        if a<=t<=b and check:
            answer += 1
            chickens[i][1] = False
            break

print(answer)
