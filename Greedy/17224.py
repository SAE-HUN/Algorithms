n, l, k = map(int, input().split())
can_solve = {'hard':0, 'easy':0}

for _ in range(n):
    sub1, sub2 = map(int, input().split())
    if sub2 <= l:
        can_solve['hard'] += 1
    elif sub1 <= l:
        can_solve['easy'] += 1

solve_hard = min(k, can_solve['hard'])
k -= solve_hard
answer = 140*solve_hard
answer += 100*min(k, can_solve['easy'])

print(answer)
