def show_board():				#draws a board which is held in a list of lists
	for i in range(3):
		for j in range(3):
			print(plansza[i][j], end='')  #empty 'end' argument in print statement to avoid printing new line
		print('\n')

def player_move(symbol):		#one function for both players 'symbol' can be 'X' or 'O'
	print(f'Player: {symbol} move: ')  
	choice = input('Select field: 1-9 ')
	if choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
		print('Wrong move!')
		player_move(symbol)
	if choice == '1':
		i = 0
		j = 0
	if choice == '2':
		i = 0
		j = 1
	if choice == '3':
		i = 0
		j = 2
	if choice == '4':
		i = 1
		j = 0
	if choice == '5':
		i = 1
		j = 1
	if choice == '6':
		i = 1
		j = 2
	if choice == '7':
		i = 2
		j = 0
	if choice == '8':
		i = 2
		j = 1
	if choice == '9':
		i = 2
		j = 2
	if plansza[i][j] != [' ']:
		print('Place taken, please try again')
		player_move(symbol)
	else:
		plansza[i][j] = [symbol]
	return plansza

def win_check(symbol):
	if plansza[0][0] == [symbol] and plansza[0][1] == [symbol] and plansza[0][2] == [symbol] or plansza[1][0] == [symbol] and plansza[1][1] == [symbol] and plansza[1][2] == [symbol] or plansza[2][0] == [symbol] and plansza[2][1] == [symbol] and plansza[2][2] == [symbol] or plansza[0][0] == [symbol] and plansza[1][0] == [symbol] and plansza[2][0] == [symbol] or plansza[0][1] == [symbol] and plansza[1][1] == [symbol] and plansza[2][1] == [symbol] or plansza[0][2] == [symbol] and plansza[1][2] == [symbol] and plansza[2][2] == [symbol] or plansza[0][0] == [symbol] and plansza[1][1] == [symbol] and plansza[2][2] == [symbol] or plansza[2][0] == [symbol] and plansza[1][1] == [symbol] and plansza[0][2] == [symbol]:
		print(f'[{symbol}] in line! Player 1 wins!')
		return True

plansza = [[[' '],[' '],[' ']], [[' '],[' '],[' ']], [[' '],[' '],[' ']]]

show_board()
player_move('X')
for i in range(4):
	show_board()
	player_move('O')
	if win_check('O') == True:
		break
	show_board()
	player_move('X')
	if win_check('X') == True:
		break
show_board()
