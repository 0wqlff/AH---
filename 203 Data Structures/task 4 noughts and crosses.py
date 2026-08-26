board = [
	['X', 'X', 'O'],
	['X', 'O', 'O'],
	['O', 'O', 'X']
]
for row in range(3):
	print(board[row])
 
winner = ''
for row in range(3):
	if board[row][0]==board[row][1]==board[row][2]:
		winner=board[row][0]

# TODO 1: check rows
for col in range(3):
	if board[0][col]==board[1][col]==board[2][col]:
		winner=board[0][col]

# TODO 2: check columns
for r in range(3):
	if board[1][1]==board[0][0]==board[2][2] or board[1][1]==board[0][2]==board[2][0]:
		winner=board[1][1]
# TODO 3: check diagonals
 
# TODO 4: report the result
if winner == '':
	print('No winner')
else:
    print(winner, 'has won')
