import sys

def find_parent(x):
	if parents[x] == x:
		return x
	p = find_parent(parents[x])
	parents[x] = p
	return p
	
def union(x, y):
	x = find_parent(x)
	y = find_parent(y)
	parents[x] = y

input = sys.stdin.readline
n = int(input().strip())
max_d = 0
assignments = []

for _ in range(n):
	d, w = map(int, input().split())
	assignments.append((d, w))
	max_d = max(max_d, d)
	
assignments.sort(key=lambda x:x[1], reverse=True)
parents = {i:i for i in range(max_d+1)}
answer = 0

for d, w in assignments:
	parent = find_parent(d)
	if parent:
		answer += w
		union(parent, parent-1)
		
print(answer)
