t = int(input())

for _ in range(t):
	n = int(input())
	stocks = list(map(int, input().split()))
	answer = 0
	max_stock = stocks[-1]
	
	for i in range(n-1, -1, -1):
		if stocks[i] > max_stock:
			max_stock = stocks[i]
		else:
			answer += max_stock - stocks[i]
			
	print(answer)
