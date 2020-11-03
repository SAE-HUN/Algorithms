# your code goes here
def solution(x, y):
	if y==c-1:
		return True
	
	for d in dx:
		if 0<=x+d<r and not visited[x+d][y+1] and maps[x+d][y+1]=='.':
			visited[x+d][y+1] = True
			if solution(x+d, y+1):
				return True
				
	return False

r, c = map(int, input().split())
maps = [list(input().strip()) for _ in range(r)]

dx = [-1, 0, 1]
visited = [[False]*c for _ in range(r)]
ans = 0
for i in range(r):
	if solution(i, 0):
		ans += 1
		
print(ans)
