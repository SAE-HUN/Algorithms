n, s, r = map(int, input().split())
kayak = [1 for _ in range(n)]

for team in map(int, input().split()):
    kayak[team-1] -= 1

for team in map(int, input().split()):
    kayak[team-1] += 1

for i, k in enumerate(kayak):
    if k==0:
        if i>0 and kayak[i-1]>1:
            kayak[i] += 1
            kayak[i-1] -= 1
        elif i<n-1 and kayak[i+1]>1:
            kayak[i] += 1
            kayak[i+1] -= 1

print(kayak.count(0))
