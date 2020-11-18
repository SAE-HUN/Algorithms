n = int(input())
employees = list(map(int, input().split()))

ranks = [0] * n
tree = {i:[] for i in range(n)}
max_rank = 0

for i in range(1, n):
    ranks[i] = ranks[employees[i]] + 1
    max_rank = max(max_rank, ranks[i])
    tree[employees[i]].append(i)

layers = []
for _ in range(max_rank+1):
    layers.append([])

for i in range(n):
    rank = ranks[i]
    layers[rank].append(i)
layers.reverse()

costs = {i:0 for i in range(n)}
for layer in layers[1:]:
    for parents in layer:
        children = tree[parents]
        children_cost = []
        
        for child in children:
            cost = costs[child]
            children_cost.append(cost)
        
        children_cost.sort(reverse=True)
        max_cost = 0
        
        for i, cost in enumerate(children_cost):
            max_cost = max(max_cost, cost+i+1)
        
        costs[parents] = max_cost

print(costs[0])
