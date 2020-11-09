n = int(input())
milks = [int(input()) for _ in range(n)]
milks.sort(reverse=True)
answer = 0

for i, milk in enumerate(milks):
    if (i+1)%3 != 0:
        answer += milk

print(answer)
