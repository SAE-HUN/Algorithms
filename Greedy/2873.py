def get_min_block():
	min_pleasure = 1001
	for i in range(r):
		for j in range(c):
			if (i+j)%2 != 0:
				if table[i][j] < min_pleasure:
					min_pleasure = table[i][j]
					min_block = (i, j)
	return min_block

r, c = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(r)]
answer = []

if r%2 != 0:
	for i in range(r//2):
		answer.append('R'*(c-1))
		answer.append('D')
		answer.append('L'*(c-1))
		answer.append('D')
	answer.append('R'*(c-1))
elif c%2 != 0:
	for i in range(c//2):
		answer.append('D'*(r-1))
		answer.append('R')
		answer.append('U'*(r-1))
		answer.append('R')
	answer.append('D'*(r-1))
else:
	min_block = get_min_block()
	for i in range(min_block[1]//2):
		answer.append('D'*(r-1))
		answer.append('R')
		answer.append('U'*(r-1))
		answer.append('R')

	for i in range(min_block[0]//2):
		answer.append('RDLD')
	if min_block[1]%2 == 0:
		answer.append('RD')
	else:
		answer.append('DR')
	for i in range((r-min_block[0]-1)//2):
		answer.append('DLDR')

	for i in range((c-min_block[1]-1)//2):
		answer.append('R')
		answer.append('U'*(r-1))
		answer.append('R')
		answer.append('D'*(r-1))

print(''.join(answer))
