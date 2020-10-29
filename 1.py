def show_board():
	for i in range(3):
		for j in range(3):
			print(plansza[i][j], end='')
		print('\n')

def player_move(symbol):
	try:
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
	except:
		pass

# def player_move_X(plansza):
# 	try:
# 		print('Player 1: Where to place \'X\'?')
# 		i = int(input('Select row: 1-3'))
# 		j = int(input('Select column: 1-3'))
# 		if plansza[i-1][j-1] != [' ']:
# 			print('Place taken, please try again')
# 			player_move_X(plansza)
# 		else:
# 			plansza[i-1][j-1] = ['X']
# 		return plansza
# 	except IndexError:
# 		print('Wrong value!')
# 		player_move_X(plansza)
# 	except ValueError:
# 		print('Wrong value!')
# 		player_move_X(plansza)

# def player_move_O(plansza):
# 	try:
# 		print('Player 2: Where to place \'O\'?')
# 		i = int(input('Select row: 1-3'))
# 		j = int(input('Select column: 1-3'))
# 		if plansza[i-1][j-1] != [' ']:
# 			print('Place taken, please try again')
# 			player_move_O(plansza)
# 		else:
# 			plansza[i-1][j-1] = ['O']
# 		return plansza
# 	except IndexError:
# 		print('Wrong value!')
# 		player_move_O(plansza)
# 	except ValueError:
# 		print('Wrong value!')
# 		player_move_0(plansza)

def win_check(symbol):
	if plansza[0][0] == [symbol] and plansza[0][1] == [symbol] and plansza[0][2] == [symbol] or plansza[1][0] == [symbol] and plansza[1][1] == [symbol] and plansza[1][2] == [symbol] or plansza[2][0] == [symbol] and plansza[2][1] == [symbol] and plansza[2][2] == [symbol] or plansza[0][0] == [symbol] and plansza[1][0] == [symbol] and plansza[2][0] == [symbol] or plansza[0][1] == [symbol] and plansza[1][1] == [symbol] and plansza[2][1] == [symbol] or plansza[0][2] == [symbol] and plansza[1][2] == [symbol] and plansza[2][2] == [symbol] or plansza[0][0] == [symbol] and plansza[1][1] == [symbol] and plansza[2][2] == [symbol] or plansza[2][0] == [symbol] and plansza[1][1] == [symbol] and plansza[0][2] == [symbol]:
		print(f'[{symbol}] in line! Player 1 wins!')
		return True

plansza = ([[' '],[' '],[' ']], [[' '],[' '],[' ']], [[' '],[' '],[' ']])

show_board()
player_move('X')
#player_move_X(plansza)
for i in range(4):
	show_board()
	player_move('O')
	#player_move_O(plansza)
	if win_check('O') == True:
		break
	show_board()
	player_move('X')
	#player_move_X(plansza)
	if win_check('X') == True:
		break
show_board()