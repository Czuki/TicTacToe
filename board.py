def show_board(plansza):				#draws a board which is held in a list of lists
	for i in range(3):
		for j in range(3):
			print(plansza[i][j], end='')  #empty 'end' argument in print statement to avoid printing new line
		print('\n')

def draw_board():
	return [[[' '], [' '], [' ']], [[' '], [' '], [' ']], [[' '], [' '], [' ']]]