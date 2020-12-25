n = int(input())
answer = 1

while n>4:
    n -= 3
    answer *= 3
    answer %= 10007

print(answer*n%10007)
