t = int(input())
for _ in range(t):
	n = int(input())
	logs = list(map(int, input().split()))
	logs.sort()
	
	arr = []
	for i in range(n):
		a = logs.pop(0)
		if i%2==0:
			arr.append(a)
		else:
			arr.insert(0, a)
			
	answer = 0
	for i in range(n):
		l = abs(arr[i] - arr[i-1])
		try:
			r = abs(arr[i] - arr[i+1])
		except:
			r = abs(arr[i] - arr[0])
		answer = max(answer, max(l, r))
	print(answer)