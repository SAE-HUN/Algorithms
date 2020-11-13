import sys

n = int(input())
weights = list(map(int, input().split()))

weights.sort()
total = 0
for weight in weights:
    if weight > total+1:
        print(total+1)
        sys.exit()
    total += weight

print(total+1)
