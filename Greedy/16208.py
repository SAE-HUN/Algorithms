n = int(input())
rods = sorted(map(int, input().split()))
answer, total = 0, sum(rods)

for i in range(n-1):
    total -= rods[i]
    answer += rods[i]*total

print(answer)
