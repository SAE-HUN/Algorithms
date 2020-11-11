n = int(input())
ballons = list(map(int, input().split()))

check = [0] * (max(ballons)+2)
answer = 0

for ballon in ballons:
    if check[ballon+1]:
        check[ballon+1] -= 1
    else:
        answer += 1
    check[ballon] += 1

print(answer)
