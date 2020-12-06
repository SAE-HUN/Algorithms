(n, m), cards = map(int, input().split()), [*map(int, input().split())]

answer = 0
for i in range(n):
    total = cards[i]
    for j in range(i+1, n):
        total += cards[j]
        for k in range(j+1, n):
            total += cards[k]
            if total<=m and total>answer:
                answer = total
            total -= cards[k]
        total -= cards[j]

print(answer)
