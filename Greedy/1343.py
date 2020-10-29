import sys

board = input().split('.')

for i, cells in enumerate(board):
	if len(cells) % 2 != 0:
		print(-1)
		sys.exit()
	else:
		if len(cells) % 4 == 0:
			board[i] = cells.replace('X', 'A')
		else:
			board[i] = cells[:-2].replace('X', 'A') + cells[-2:].replace('X', 'B')
print('.'.join(board))
