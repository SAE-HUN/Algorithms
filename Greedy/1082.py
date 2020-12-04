n = int(input())
costs = [*map(int, input().split())]
money = int(input())

min_cost = min(costs)
min_cost_num = costs.index(min_cost)

answer = [min_cost_num]*(money//min_cost)
money %= min_cost

while len(answer) and answer[0]==0:
    max_num = 0
    money += costs[0]
    
    for i in range(n):
        if costs[i]<=money:
            max_num = max(max_num, i)
    
    if max_num!=0:
        answer[0] = max_num
        money -= costs[max_num]
    else:
        answer.pop()

for i in range(len(answer)):
    money += costs[answer[i]]
    max_num = answer[i]
    
    for j in range(n):
        if costs[j]<=money:
            max_num = max(max_num, j)
    
    if max_num!=answer[i]:
        answer[i] = max_num
        money -= costs[max_num]
    else:
        money -= costs[answer[i]]

print(''.join(map(str, answer)) if answer else 0)
