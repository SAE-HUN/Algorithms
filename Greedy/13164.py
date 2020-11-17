n, k = map(int, input().split())
children = list(map(int, input().split()))

diffs = []
for i in range(n-1):
    diffs.append(children[i+1] - children[i])

diffs.sort()
print(sum(diffs[:n-k]))
