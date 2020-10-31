n, m = map(int,  input().split())
j = int(input())
basket, answer = [1, m], 0

for _ in range(j):
	apple = int(input())
	if apple < basket[0]:
		answer += basket[0] - apple
		basket[0] = apple
		basket[1] = basket[0] + m - 1
	elif apple > basket[1]:
		answer += apple - basket[1]
		basket[1] = apple
		basket[0] = basket[1] - m + 1

print(answer)
