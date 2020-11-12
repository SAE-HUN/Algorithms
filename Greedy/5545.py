n = int(input())
a, b = map(int, input().split())
c = int(input())
ds = [int(input()) for _ in range(n)]

ds.sort(reverse=True)
calory_per_cost = c // a
calory_sum = 0

for i, d in enumerate(ds):
    calory_sum += d
    next_calory = (c + calory_sum) // (a+b*(i+1))
    
    if calory_per_cost <= next_calory:
        calory_per_cost = next_calory
    else:
        break

print(calory_per_cost)
