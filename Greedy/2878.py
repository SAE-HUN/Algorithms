m, n = map(int, input().split())
_sum, friends = 0, []

for _ in range(n):
    candy = int(input())
    _sum += candy
    friends.append(candy)

friends.sort()
answer, lack = 0, _sum-m

for i, friend in enumerate(friends):
    candy = min(friend, lack//(n-i))
    answer += candy**2
    answer %= 2**64
    lack -= candy

print(answer)
