n, l = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

result = 0
index = 0
pipes = [False] * n

while(True):
	if pipes[n-1] == True:
		break
	for i in range(index, n):
		if arr[i] - arr[index] + 1 > l:
			break
		pipes[i] = True
	index = i
	result += 1
	
print(result)
