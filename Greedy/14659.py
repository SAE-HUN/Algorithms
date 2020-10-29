n = int(input())
mountains = list(map(int, input().split()))
answer = 0
temp = 0
current_mountain = mountains[0]

for mountain in mountains[1:]:
	if mountain > current_mountain:
		answer = max(answer, temp)
		current_mountain = mountain
		temp = 0
		continue
	temp += 1
answer = max(answer, temp)
	
print(answer)
