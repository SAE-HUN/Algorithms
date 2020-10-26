def lower_bound(x):
	l = 0
	r = len(D)
	while l!=r:
		m = (l+r) // 2
		if D[m] == x:
			return m
		elif D[m] < x:
			l = m + 1
		elif D[m] > x:
			r = m
	
	return l

n = int(input())
arr = list(map(int, input().split()))
D = [arr[0]]

for i in range(1, n):
	if D[-1] < arr[i]:
		D.append(arr[i])
	else:
		if D[-1] == arr[i]:
			continue
		elif D[-1] > arr[i]:
			idx = lower_bound(arr[i])
			D[idx] = arr[i]
			
print(len(D))
