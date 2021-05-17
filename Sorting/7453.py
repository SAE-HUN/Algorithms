from collections import Counter

n = int(input())
a = []
b = []
c = []
d = []

for _ in range(n):
    e = list(map(int, input().split()))
    a.append(e[0])
    b.append(e[1])
    c.append(e[2])
    d.append(e[3])

ab = []
cd = {}
for i in range(n):
    for j in range(n):
        ab.append(a[i]+b[j])
        cd[c[i]+d[j]] = cd.get(c[i]+d[j], 0) + 1

answer = 0
for key in ab:
    answer += cd.get(-key, 0)

print(answer)
