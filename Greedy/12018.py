n, m = map(int, input().split())

mileages = []
for _ in range(n):
    p, l = map(int, input().split())
    people = list(map(int, input().split()))
    people.sort(reverse=True)
    
    if p >= l:
        mileages.append(people[l-1])
    else:
        mileages.append(1)

mileages.sort()
answer = 0
sum_mileage = 0

for mileage in mileages:
    if mileage > 36:
        continue
    sum_mileage += mileage
    if sum_mileage > m:
        break
    answer += 1

print(answer)
