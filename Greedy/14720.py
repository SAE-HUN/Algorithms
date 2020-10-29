n = int(input())
stores = list(map(int, input().split()))
next, answer = 0, 0

for store in stores:
	if store == next:
		answer += 1
		if store == 2:
			next = 0
		else:
			next += 1
			
print(answer)
