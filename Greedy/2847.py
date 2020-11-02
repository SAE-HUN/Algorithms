n = int(input())
scores = [int(input()) for _ in range(n)]
answer = 0

for i in range(n-1, 0, -1):
	if scores[i-1]>scores[i]-1:
		answer += scores[i-1] - (scores[i] - 1)
		scores[i-1] = scores[i] - 1
		
print(answer)
