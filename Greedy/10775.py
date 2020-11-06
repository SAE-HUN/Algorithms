import sys
input = sys.stdin.readline
g = int(input().strip())
p = int(input().strip())
planes = [int(input().strip()) for _ in range(p)]
parents = {i:i for i in range(g+1)}

def find_parent(x):
	if parents[x] == x:
		return x
	p = find_parent(parents[x])
	parents[x] = p
	return parents[x]
	
def union(x, y):
	x = find_parent(x)
	y = find_parent(y)
	parents[x] = y
	
answer = 0
for plane in planes:
	x = find_parent(plane)
	if x == 0:
		break
	union(x, x-1)
	answer += 1
	
print(answer)
